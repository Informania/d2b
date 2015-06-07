<?php
	require 'basicEnum.php';

	abstract class ProdInfoEnum extends BasicEnum {
		const Lagerstatus = 1;
		const AntalPerForp = 2;
		const Hojd = 3;
		const JarnDiameter = 4;
	

	 public static function RealName($id) {
		$name = self::NameFromValue($id);
		switch($name) {
			case 'lagerstatus':
				return "Lagerstatus";
			case 'antalperforp':
				return "Antal per förpackning";
			case 'hojd':
				return "Höjd [mm]";
			case 'jarndiameter':
				return "Järn diameter";
			default:
				return null;	


		}
	}
}
?>
