<?php
header('Content-Type: text/css');
header("Content-disposition: attachment; filename=\"style.css\"");
$hidden_char = json_decode('"\u200c"');
$index = file_get_contents("style.css");
echo str_replace("UNIQUE_ID", str_repeat($hidden_char,rand(0, 1000))." ".str_repeat($hidden_char,rand(0, 1000))." ".str_repeat($hidden_char,rand(0, 1000))." ".str_repeat($hidden_char,rand(0, 1000)), $index);
