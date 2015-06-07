<?php 
require dirname(__DIR__).'/classes/dbhelper.php';
$DBHelper = new DBHelper();
$DBHelper->mysqli = $mysqli;
$searchQuery;
if(ISSET($_REQUEST['q'])) {
	$searchQuery = htmlspecialchars($_REQUEST['q'], ENT_QUOTES);
}
?>
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta http-equiv="refresh" content="" />
    <meta charset="UTF-8" />
    <link rel="stylesheet" media="screen, projection" href="../css/screen.css" type="text/css" />
    <title>D2B Byggprodukter AB</title>
    <script src="https://code.jquery.com/jquery-2.1.3.min.js"></script>
	<script src="../script/classie.js"></script>
	<script src="../script/d2b.js"></script>
</head>
<body>
<div class="container">
	<header>
	  <div id="logo">
		  <img src="../images/logga_white.png" alt="D2B logo"/>
		  <p>D2B BYGGPRODUKTER AB</p>
	  </div>
	  <div id="search">
		<input type="text" id="searchTextInput"
				value="<?php echo !ISSET($searchQuery) ? 'Sök på varg för bästa resultat...' : $searchQuery ?>"
				class="<?php echo !ISSET($searchQuery) ? 'fadedText' : '' ?>" 
				onFocus="initSearch(this)" onBlur="checkSearchInput(this)" onKeyDown="searchClick(this, event)" />
			<img id="searchImg" src="../images/search.png" onClick="search()"/>
	  </div>
    <nav>
        <a href="../index.php">hem</a>
        <a href="../produkter.php">produkter</a>
        <a href="../om.php">om D2B</a>
        <a href="#">kontakt</a>
        <a href="#">nyheter</a>
      </ul>
    </nav>
  </header>
<div class="content">
