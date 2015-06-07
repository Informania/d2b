<?php
require dirname(__DIR__).'/../../d2bconf.php';
require 'dbmodels.php';
class DBHelper {
	var $mysqli;

	public function GetProductsByGroup($group)
	{
		$query = sprintf("SELECT id, namn, beskrivning, bild, produktgrupp_id FROM Produkt
					WHERE produktgrupp_id = 
						(SELECT id FROM produkt_grupp WHERE namn = '%s')", $group);
		$result = $this->mysqli->query($query);
		$products = array();
		while($row = $result->fetch_assoc())
		{
			$product = new Product();
			$product->id = $row['id'];
			$product->name = $row['namn'];
			$product->desc = $row['beskrivning'];
			$product->img = $row['bild'];
			$product->group_id = $row['produktgrupp_id'];
			array_push($products, $product);
		}

		return $products;
	}

	public function GetProductById($prodId) 
	{
		$query = sprintf("SELECT id, namn, beskrivning, bild, produktgrupp_id FROM produkt
			WHERE id = %d", $prodId);
		$result = $this->mysqli->query($query);
		$row = $result->fetch_assoc();
		$product = new Product();
		$product->id = $row['id'];
		$product->name = $row['namn'];
		$product->desc = $row['beskrivning'];
		$product->img = $row['bild'];
		$product->group_id = $row['produktgrupp_id'];
		return $product;
	}

	public function GetInfoNamesByProductId($prodId) 
	{
		$query = sprintf("SELECT id, namn, ordning FROM info_namn where id in (
			SELECT info_namn_id FROM produkt_info where produkt_id = '%d')
			ORDER BY ordning", $prodId);
		$result = $this->mysqli->query($query);
		$infoNames = array();
		while($row = $result->fetch_assoc())
		{
			$infoName = new InfoName();
			$infoName->id = $row['id'];
			$infoName->name = $row['namn'];
			$infoName->order = $row['ordning'];
			array_push($infoNames, $infoName);
		}

		return $infoNames;
	}
	
	### Returns a nested array of productinfos, kept together by colledtionNo
	public function GetProductInfoValuesByProductId($prodId) 
	{
		$query = sprintf("SELECT pi.id, produkt_id, info_namn_id, varde, samlingsid 
			FROM produkt_info pi
			JOIN info_namn inf ON pi.info_namn_id = inf.id
			WHERE pi.produkt_id = '%d'
			ORDER BY samlingsid, inf.ordning", $prodId);
		$result = $this->mysqli->query($query);

		# Each productinfo needs to be kept together by collectionId so they dont mix.
		# This gives infovalues = [ [value, value, value] , [value, value, value] ] etc.
		$productInfoValues = array();
		$productInfos = array();
		$collection = 1;
		while($row = $result->fetch_assoc())
		{	
			if($collection != $row['samlingsid'])
			{
				array_push($productInfoValues, $productInfos);
				$collection = $row['samlingsid'];
				$productInfos = array();	
			}
			$productInfo = new ProductInfo();
			$productInfo->id = $row['id'];
			$productInfo->productId = $row['produkt_id'];
			$productInfo->infoNameId = $row['info_namn_id'];
			$productInfo->value = $row['varde'];
			$productInfo->collectionNo = $row['samlingsid'];
			
			array_push($productInfos, $productInfo);
		}
		array_push($productInfoValues, $productInfos); # Push the last row in the array
		return $productInfoValues;
	}

}
?>
