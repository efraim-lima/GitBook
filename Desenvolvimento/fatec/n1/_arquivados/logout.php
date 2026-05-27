<html><head><title>Duck Tech - Logout</title>
<meta http-equiv="Cache-Control" content="No-Cache">
</head><body>
<?php
session_start();
session_destroy();
echo "Voce foi desconectado com sucesso.";
echo "<br><a href='javascript:history.back()'>Voltar</a>";
?>
</body></html>
