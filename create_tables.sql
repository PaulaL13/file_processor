
CREATE TABLE `sabadell_cabecera_fichero` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_fichero` varchar(100) DEFAULT NULL,
  `tipo_registro` varchar(2) DEFAULT NULL,
  `fecha_proceso` date DEFAULT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `fecha_final` date DEFAULT NULL,
  `datos_adicionales` varchar(188) DEFAULT NULL,
  `fila_completa` varchar(220) DEFAULT '',
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre_fichero` (`fila_completa`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=latin1;


CREATE TABLE `sabadell_cabecera_remesa` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `cabecera_fichero_id` int(11) NOT NULL,
  `tipo_registro` varchar(2) DEFAULT NULL,
  `numero_contrato` varchar(15) DEFAULT NULL,
  `numero_comercio` varchar(10) DEFAULT NULL,
  `cuenta_comercio` varchar(20) DEFAULT NULL,
  `oficina_gestora` varchar(4) DEFAULT NULL,
  `fecha_proceso` date DEFAULT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `fecha_final` date DEFAULT NULL,
  `datos_adicionales` varchar(139) DEFAULT NULL,
  `fila_completa` varchar(220) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fila_completa` (`fila_completa`),
  KEY `cabecera remesa key` (`cabecera_fichero_id`),
  CONSTRAINT `cabecera remesa key` FOREIGN KEY (`cabecera_fichero_id`) REFERENCES `sabadell_cabecera_fichero` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=latin1;


CREATE TABLE `sabadell_cola_comercio` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `cabecera_fichero_id` int(11) DEFAULT NULL,
  `tipo_registro` varchar(2) DEFAULT NULL,
  `datos_adicionales` varchar(25) DEFAULT NULL,
  `numeros_operaciones_comercio` varchar(9) DEFAULT NULL,
  `importe_total` decimal(13,2) DEFAULT NULL,
  `signo` varchar(1) DEFAULT NULL,
  `mas_datos_adicionales` varchar(170) DEFAULT NULL,
  `fila_completa` varchar(220) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fila_completa` (`fila_completa`),
  KEY `cola comercio key` (`cabecera_fichero_id`),
  CONSTRAINT `cola comercio key` FOREIGN KEY (`cabecera_fichero_id`) REFERENCES `sabadell_cabecera_fichero` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=latin1;

CREATE TABLE `sabadell_cola_fichero` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `cabecera_fichero_id` int(11) DEFAULT NULL,
  `tipo_registro` varchar(2) DEFAULT NULL,
  `numero_comercios` varchar(9) DEFAULT NULL,
  `datos_adicionales` varchar(25) DEFAULT NULL,
  `numero_operaciones` varchar(9) DEFAULT NULL,
  `importe_total` decimal(13,2) DEFAULT NULL,
  `signo` varchar(1) DEFAULT NULL,
  `mas_datos_adicionales` varchar(161) DEFAULT NULL,
  `fila_completa` varchar(220) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fila_completa` (`fila_completa`),
  KEY `cabecera fichero id` (`cabecera_fichero_id`),
  CONSTRAINT `prueba` FOREIGN KEY (`cabecera_fichero_id`) REFERENCES `sabadell_cabecera_fichero` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=latin1;


CREATE TABLE `sabadell_registro_operacion` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `cabecera_fichero_id` int(11) DEFAULT NULL,
  `tipo_registro` varchar(2) DEFAULT NULL,
  `fecha_valoracion_abono` date DEFAULT NULL,
  `numero_remesa` varchar(10) DEFAULT NULL,
  `numero_factura_operacion` varchar(12) DEFAULT NULL,
  `oficina_remesa` varchar(4) DEFAULT NULL,
  `tarjeta` varchar(20) DEFAULT NULL,
  `clase_tarjeta` varchar(2) DEFAULT NULL,
  `modalidad_pago` varchar(1) DEFAULT NULL,
  `entidad_tarjeta_emisora` varchar(1) DEFAULT NULL,
  `fecha_operacion` date DEFAULT NULL,
  `hora_operacion` time DEFAULT NULL,
  `numero_autorizacion` varchar(6) DEFAULT NULL,
  `tipo_operacion` varchar(2) DEFAULT NULL,
  `captura_operacion` varchar(3) DEFAULT NULL,
  `importe_operacion` decimal(11,2) DEFAULT NULL,
  `signo_operacion` varchar(1) DEFAULT NULL,
  `tasa_descuento` decimal(5,2) DEFAULT NULL,
  `importe_descuento` decimal(9,2) DEFAULT NULL,
  `signo_descuento` varchar(1) DEFAULT NULL,
  `importe_liquido` decimal(13,2) DEFAULT NULL,
  `signo_liquido` varchar(1) DEFAULT NULL,
  `numero_tpv` varchar(13) DEFAULT NULL,
  `arn` varchar(23) DEFAULT NULL,
  `tasa_intercambio` decimal(9,6) DEFAULT NULL,
  `gastos` decimal(5,2) DEFAULT NULL,
  `datos_adicionales` varchar(1) DEFAULT NULL,
  `divisa_comercio` varchar(3) DEFAULT NULL,
  `numero_operacion` varchar(12) DEFAULT NULL,
  `codigo_razon` varchar(4) DEFAULT NULL,
  `mas_datos_adicionales` varchar(2) DEFAULT NULL,
  `importe_original` decimal(13,2) DEFAULT NULL,
  `signo_original` varchar(1) DEFAULT NULL,
  `divisa_original` varchar(3) DEFAULT NULL,
  `incluso_mas_datos_adicionales` varchar(1) DEFAULT NULL,
  `fila_completa` varchar(220) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fila_completa` (`fila_completa`),
  KEY `registro key` (`cabecera_fichero_id`),
  CONSTRAINT `registro key` FOREIGN KEY (`cabecera_fichero_id`) REFERENCES `sabadell_cabecera_fichero` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=84279 DEFAULT CHARSET=latin1;