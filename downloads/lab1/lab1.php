<?php
header('Content-Type: application/html');
header("Content-disposition: attachment; filename=\"lab1.html\"");
$hidden_char = json_decode('"\u200c"');
$index = file_get_contents("lab1.html");
echo str_replace("UNIQUE_ID", str_repeat($hidden_char,rand(0, 1000))." ".str_repeat($hidden_char,rand(0, 1000))." ".str_repeat($hidden_char,rand(0, 1000))." ".str_repeat($hidden_char,rand(0, 1000)), $index);
