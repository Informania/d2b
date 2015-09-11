<?php
abstract class BasicEnum {
    private static $constCacheArray = NULL;

    private static function getConstants() {
        if (self::$constCacheArray == NULL) {
            self::$constCacheArray = [];
        }
        $calledClass = get_called_class();
        if (!array_key_exists($calledClass, self::$constCacheArray)) {
            $reflect = new ReflectionClass($calledClass);
            self::$constCacheArray[$calledClass] = $reflect->getConstants();
        }
        return self::$constCacheArray[$calledClass];
	}

	protected static function NameFromValue($id) {
		$constants = self::getConstants();
		$keys = array_map('strtolower', array_keys($constants));
		return $keys[$id-1];
	}
	protected static function ValueFromName($name) {
		$constants = self::getConstants();
		return $constants[$name];
	}
}


?>
