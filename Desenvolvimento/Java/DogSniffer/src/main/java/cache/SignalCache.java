package cache;

import java.util.*;
import java.util.concurrent.*;

/**
 * SignalCache é o "coração" da aplicação.
 *
 * Ele é um cache thread-safe que armazena CacheEntry por MAC address.
 * Thread-safe significa que múltiplas threads podem ler/escrever
 * ao mesmo tempo sem corromper os dados.
 *
 * Usamos ConcurrentHashMap para isso — é como um HashMap normal,
 * mas seguro para uso em múltiplas threads.
 *
 * A cada 5 segundos, uma thread de limpeza remove entradas antigas.
 *
 * Padrão Singleton: só existe UMA instância do cache na aplicação.
 * Isso garante que todos os módulos compartilhem o mesmo cache.
 */
public class SignalCache {

    private static volatile SignalCache instance;
    private final ConcurrentHashMap<String, CacheEntry> cache;
    private static final long TTL_MS = 5000;
    private final ScheduledExecutorService scheduler;

    /**
     * Construtor privado — parte do padrão Singleton.
     * Ninguém de fora pode criar uma instância diretamente.
     */
    private SignalCache() {
        this.cache     = new ConcurrentHashMap<>();
        this.scheduler = Executors.newSingleThreadScheduledExecutor(r -> {
           
            Thread t = new Thread(r, "cache-cleaner");
            t.setDaemon(true);
            return t;
        });

        scheduler.scheduleAtFixedRate(
            this::cleanExpiredEntries,
            5, 5, TimeUnit.SECONDS
        );
    }

    /**
     * Método de acesso ao Singleton.
     * "synchronized" garante que só uma thread inicializa o objeto.
     * Double-checked locking para performance.
     */
    public static SignalCache getInstance() {
        if (instance == null) {
            synchronized (SignalCache.class) {
                if (instance == null) {
                    instance = new SignalCache();
                }
            }
        }
        return instance;
    }

    /**
     * Atualiza ou cria uma entrada no cache.
     *
     * computeIfAbsent: se o MAC não existe, cria uma nova CacheEntry.
     * Se já existe, retorna a existente.
     * Em seguida, atualizamos os campos e chamamos touch() para
     * renovar o timestamp.
     */
    public CacheEntry updateEntry(String macAddress, String ssid) {
        CacheEntry entry = cache.computeIfAbsent(
            macAddress,
            mac -> new CacheEntry(mac, ssid)
        );
        if (ssid != null && !ssid.isEmpty()) {
            entry.setSsid(ssid);
        }
        entry.touch(); // renova o timestamp
        return entry;
    }

    /**
     * Busca uma entrada pelo MAC address.
     * Retorna Optional.empty() se não encontrar.
     *
     * Optional é uma forma segura de lidar com valores que podem ser null.
     * Evita NullPointerException.
     */
    public Optional<CacheEntry> getEntry(String macAddress) {
        return Optional.ofNullable(cache.get(macAddress));
    }

    /**
     * Retorna todas as entradas do cache como lista imutável.
     * Usamos new ArrayList<>() para criar uma cópia — assim
     * o chamador não pode modificar o cache diretamente.
     */
    public List<CacheEntry> getAllEntries() {
        return new ArrayList<>(cache.values());
    }

    /**
     * Retorna quantas entradas existem no cache.
     */
    public int size() {
        return cache.size();
    }

    /**
     * Limpeza de entradas expiradas.
     *
     * entrySet().removeIf() percorre o mapa e remove
     * qualquer entrada cuja idade seja maior que o TTL.
     *
     * Isso é chamado automaticamente a cada 5 segundos pelo scheduler.
     */
    private void cleanExpiredEntries() {
        int before = cache.size();

        cache.entrySet().removeIf(entry ->
            entry.getValue().getAgeMillis() > TTL_MS
        );

        int removed = before - cache.size();
        if (removed > 0) {
            System.out.printf("[Cache] 🧹 %d entradas expiradas removidas. Total: %d%n",
                removed, cache.size());
        }
    }

    /**
     * Encerra o scheduler ao fechar a aplicação.
     * Bom hábito: sempre liberar recursos ao terminar.
     */
    public void shutdown() {
        scheduler.shutdown();
    }
}