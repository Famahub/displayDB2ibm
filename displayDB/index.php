<?php
$servername = "localhost"; // Adresse du serveur MariaDB
$username = "famaroot"; // Votre nom d'utilisateur MariaDB
$password = "famaroot"; // Votre mot de passe MariaDB
$database = "logp"; // Le nom de votre base de données MariaDB

try {
    $conn = new PDO("mysql:host=$servername;dbname=$database", $username, $password);
    // Configuration pour gérer les erreurs de connexion
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Connexion réussie";
}
catch(PDOException $e) {
    echo "La connexion a échoué : " . $e->getMessage();
}
?>
