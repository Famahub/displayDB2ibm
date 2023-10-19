<?php
$dsn = 'odbc:iSeries Access ODBC Drive'; // Remplacez avec le nom de votre source de données ODBC
$user = 'famaroot';
$password = 'famaroot';

try {
    $dbh = new PDO($dsn, $user, $password);
    echo "Connexion réussie";
} catch (PDOException $e) {
    echo 'Erreur de connexion : ' . $e->getMessage();
}
?>
