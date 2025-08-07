<?php

require_once __DIR__ . '/vendor/autoload.php';

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();

$wsdl = "http://clswcorrientes.smartmovepro.net/ModuloParadas/SWParadas.asmx?WSDL";

$client = new SoapClient($wsdl, [
  'trace' => true,
  'exceptions' => true
]);
$params = [
  "usuario" => $_ENV['USUARIO'],
  "clave" => $_ENV['CLAVE'],
  "localidad" => "Corrientes",
  "provincia" => "Corrientes",
  "pais" => "Argentina",
  "isSublinea" => false,
];

try {
  $response = $client->RecuperarLineaPorLocalidad($params);
  print_r($response);
  echo $client->__getLastRequest();
} catch (SoapFault $e) {
  echo "Error: {$e->getMessage()}\n";
}
