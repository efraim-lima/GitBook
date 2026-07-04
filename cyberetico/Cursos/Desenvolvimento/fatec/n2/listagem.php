<html><head><title>Listagem Duck Tech</title>
<meta http-equiv="Cache-Control" content="No-Cache">
<style>
body {
    background-color: #1C1526;
    margin: 0;
    padding: 30px;
    font-size: 16px;
    color: #F2F2F2;
}
div.lista-container {
    max-width: 1200px;
    margin: 0 auto;
    background-color: #2D2540;
    padding: 25px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}
h3 { color: #F2A413; text-align: center; margin-top: 0; }
table { width: 100%; background-color: #2D2540; margin-top: 20px; border-collapse: collapse; }
th { background-color: #F2A413; color: #1C1526; padding: 10px; }
td { padding: 8px 10px; border-bottom: 1px solid #734A19; }
</style>
</head><body>
<div class="lista-container">
<h3>Funcionários Duck Tech</h3>
<?php
$host    ="localhost";
$username="root";
$password="";
$db_name ="duck_tech";
$con=mysqli_connect("$host", "$username", "$password", "$db_name") or die("cannot connect");
if (mysqli_connect_errno()) {
    echo "Falhou ao conectar ao MySQL: " . mysqli_connect_error();
    exit();
}
$sql = "select id, nome, cargo, email from funcionarios order by nome";
$result = mysqli_query($con,$sql);
if (!$result) {
    die("Erro na consulta: " . mysqli_error($con));
}else{
    echo "<table border='0' width='100%'>";
    echo "<tr><th>Num</th><th>Nome</th><th>Cargo</th><th>Email</th></tr>";
    while($row = mysqli_fetch_assoc($result)){
        echo "<tr><td>".$row['id']."</td><td>".$row['nome']."</td><td>".$row['cargo']."</td><td>".$row['email']."</td></tr>";
    }
    echo "</table>";
    echo "fim de listagem";
    mysqli_close($con);
}
?>
</div>
</body>
</html>
