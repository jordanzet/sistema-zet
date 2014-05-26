SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

--
-- Estructura de tabla para la tabla `articulo`
--

CREATE TABLE IF NOT EXISTS `articulo` (
  `id_articulo` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(30) NOT NULL,
  `precio_venta` int(11) NOT NULL,
  `precio_costo` int(11) NOT NULL,
  `stock` int(11) NOT NULL,
  `cod_tipo_articulo` int(11) NOT NULL,
  `cod_proveedor` varchar(20) NOT NULL,
  `fecha_ingreso` varchar(15) NOT NULL,
  PRIMARY KEY (`id_articulo`),
  KEY `ref_tipo_articulo_idx` (`cod_tipo_articulo`),
  KEY `ref_prov_art_idx` (`cod_proveedor`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Volcar la base de datos para la tabla `articulo`
--

INSERT INTO `articulo` (`id_articulo`, `descripcion`, `precio_venta`, `precio_costo`, `stock`, `cod_tipo_articulo`, `cod_proveedor`, `fecha_ingreso`) VALUES
(1, 'Bota Larga', 100000, 80000, 20, 19, '00003-A', '2012-11-03'),
(2, 'Bota corta', 70000, 50000, 55, 19, '00003-A', '2012-10-11'),
(3, 'Botin ', 150000, 130000, 18, 19, '00003-A', '2012-09-01'),
(4, 'Tenis ', 120000, 100000, 8, 20, '00002-2', '2012-10-02'),
(5, 'Zandalias', 50000, 30000, 59, 21, '00001-1', '2012-11-01'),
(6, 'Jeans', 90000, 70000, 18, 24, '00004-4', '2012-10-02'),
(7, 'Camisas', 50000, 30000, 12, 22, '00003-A', '2012-10-20'),
(8, 'Chaquetas', 70000, 50000, 8, 24, '00004-4', '2012-11-02'),
(9, 'Chaquetas sudadera', 60000, 40000, 20, 23, '00002-2', '2012-10-23'),
(10, 'Pantalon sudadera', 60000, 40000, 17, 23, '00002-2', '2012-10-23'),
(11, 'Sudadera completa', 100000, 80000, 20, 23, '00002-2', '2012-10-23'),
(12, 'Camisetas', 30000, 20000, 30, 24, '00005-F', '2012-10-03');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ciudad`
--

CREATE TABLE IF NOT EXISTS `ciudad` (
  `Codigo_ciudad` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre_ciudad` varchar(30) NOT NULL,
  PRIMARY KEY (`Codigo_ciudad`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=21 ;

--
-- Volcar la base de datos para la tabla `ciudad`
--

INSERT INTO `ciudad` (`Codigo_ciudad`, `Nombre_ciudad`) VALUES
(1, 'POPAYAN'),
(2, 'CALI'),
(3, 'PASTO'),
(4, 'MEDELLIN'),
(5, 'BOGOTA'),
(6, 'BARRANQUILLA'),
(7, 'CARTAGENA'),
(8, 'ARAUCA'),
(9, 'BALBOA'),
(10, 'BELALCAZAR'),
(11, 'BETANIA'),
(12, 'BOLIVAR'),
(13, 'BUCARAMANGA'),
(14, 'BUENAVENTURA'),
(15, 'CUCUTA'),
(16, 'CALDAS'),
(17, 'CAQUETA'),
(18, 'CERRITO'),
(19, 'CHIA'),
(20, 'CORDOBA');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE IF NOT EXISTS `cliente` (
  `Documento` varchar(15) NOT NULL,
  `cod_tipo_documento` int(11) NOT NULL,
  `Nombres` varchar(30) NOT NULL,
  `Apellidos` varchar(30) NOT NULL,
  `Direccion` varchar(20) DEFAULT NULL,
  `cod_ciudad` int(11) NOT NULL,
  `Telefono` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Documento`),
  KEY `cod_tipodocumento_idx` (`cod_tipo_documento`),
  KEY `ref_ciudad_idx` (`cod_ciudad`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcar la base de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`Documento`, `cod_tipo_documento`, `Nombres`, `Apellidos`, `Direccion`, `cod_ciudad`, `Telefono`) VALUES
('000031', 1, 'Carlos', 'Perez', 'Carrera 23 N 34-34', 1, '3127654323'),
('000032', 1, 'dfdfff', 'ffff', 'fffff', 1, '77777'),
('0001', 1, 'Camilo', 'Lopez', 'Calle 23 N 12-43', 2, '8239578'),
('0002', 2, 'Maria', 'Arango', 'Carrera 5 N 23-12', 1, '8253478'),
('0003', 1, 'Andres', 'Florez', 'Carrera 23 N 12A 34', 4, '3127654323'),
('0004', 1, 'Carlos', 'Marin', 'Calle 3 N 98_21', 10, '8345623'),
('0005', 1, 'Elvira', 'Orozco', 'Centro', 15, '3219843543'),
('0006', 1, 'Kevin', 'Ayala', 'Carrera 23 N 4B 23', 1, '8354624'),
('0007', 1, 'Angela', 'Hoyos', 'Calle 4 N 23 34', 3, '3217654300'),
('0008', 2, 'Marcela', 'Gomez', 'Centro', 6, NULL),
('0009', 1, 'Andres', 'Orozco', 'Calle 34 N 89 00', 1, '8219876'),
('0010', 1, 'Marlon', 'Diaz', 'Carrera 23 N 78-00', 9, '3219870987'),
('0011', 1, 'Daniela', 'Ceron', 'Centro', 1, '8236543'),
('0012', 2, 'Camilo', 'Orozco', 'Calle 21 N 23-98', 10, '3119874534'),
('0013', 1, 'Daniela', 'Ramos', 'Centro', 2, '3217653400'),
('0014', 2, 'Camilo', 'Samboni', 'Carrera 23 N45A 12', 6, '8204587'),
('0015', 1, 'Alexander', 'Romero', 'Calle 34 N 23 B 12', 2, '8340976'),
('0016', 1, 'Sebastian', 'Naranjo', 'Carrera 23 N 2 A 1', 1, '8320912'),
('0017', 2, 'Sandra', 'Castillo', 'Centro', 3, '3218769988'),
('0018', 1, 'Nicolas', 'Ospina', 'Calle 23- N 76', 1, '8230954'),
('0019', 1, 'Santiago', 'Sanchez', 'Carrera 23 N 12-23', 1, '8236521'),
('0020', 1, 'Aleja', 'Dorado', 'Calle 34 N 23 B 4', 2, '8453234'),
('0021', 2, 'andrea', 'Ruiz', 'Centro', 1, '3238765456'),
('0022', 1, 'Andres', 'Perdomo', 'Centro', 3, '8456342'),
('0023', 1, 'Dolly', 'Joaqui', 'Calle 3 N 34-12', 1, '8230943'),
('0024', 2, 'Kevin', 'Rivera', 'Centro', 1, '8342309'),
('0025', 1, 'Camila', 'Maya', 'Carrera 23 n 65-4', 1, '3150987866'),
('0026', 1, 'Camilo', 'Coral', 'Centro', 1, NULL),
('0027', 2, 'Carlos', 'Paz', 'Centro', 1, NULL),
('0028', 1, 'Cristian', 'Paz', 'Calle 34 N b34', 1, '3219870045'),
('0029', 1, 'Daniela', 'Solarte', 'Centro', 1, '8345623'),
('0030', 1, 'Diana', 'Aponte', 'Centro', 15, '8234522'),
('1032', 2, 'andres', 'juan', 'calle 34-23', 2, '326589'),
('12', 1, 'kerly andrea', 'samboni bolaños', 'los cimuneros', 1, '3113882177'),
('120', 1, 'andres', 'sanchez', 'carere 12-45', 2, '8202565'),
('123', 2, 'carlos', 'andres', 'calle 23.5', 2, '235645'),
('125', 2, 'andres', 'sanchez', 'calle 23', 2, '12545'),
('4115', 2, 'hhhhhhhh', 'hhhhhhhhhh', 'hhhhhhhhhhh', 1, 'hhhhhhhhh');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_factura`
--

CREATE TABLE IF NOT EXISTS `detalle_factura` (
  `cod_factura` varchar(20) NOT NULL,
  `cod_articulo` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `total` decimal(10,0) NOT NULL,
  PRIMARY KEY (`cod_factura`,`cod_articulo`),
  KEY `ref_facturacion_idx` (`cod_factura`),
  KEY `ref_ar_fact_idx` (`cod_articulo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcar la base de datos para la tabla `detalle_factura`
--

INSERT INTO `detalle_factura` (`cod_factura`, `cod_articulo`, `cantidad`, `total`) VALUES
('FACT-9910966', 3, 1, '150000'),
('FACT-9910966', 4, 2, '240000'),
('FACT-9910966', 5, 1, '47500');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `devolucion`
--

CREATE TABLE IF NOT EXISTS `devolucion` (
  `cod_detallefactura` varchar(20) NOT NULL,
  `cod_detallearticulo` int(11) NOT NULL,
  `Motivo` varchar(15) NOT NULL,
  `Fecha_devolucion` varchar(10) NOT NULL,
  `cantidad` int(11) NOT NULL,
  PRIMARY KEY (`cod_detallefactura`,`cod_detallearticulo`),
  KEY `ref_detallefactu_idx` (`cod_detallefactura`),
  KEY `ref_deta_art_idx` (`cod_detallearticulo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcar la base de datos para la tabla `devolucion`
--

INSERT INTO `devolucion` (`cod_detallefactura`, `cod_detallearticulo`, `Motivo`, `Fecha_devolucion`, `cantidad`) VALUES
('FACT-9910966', 3, 'pequeño', '22/1/2013', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura`
--

CREATE TABLE IF NOT EXISTS `factura` (
  `Nnm_factura` varchar(20) NOT NULL,
  `cod_cliente` varchar(15) NOT NULL,
  `Nombre_empleado` varchar(30) NOT NULL,
  `Fecha_facturacion` varchar(15) NOT NULL,
  `cod_formapago` int(11) NOT NULL,
  `total_factura` decimal(10,0) DEFAULT NULL,
  `IVA` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`Nnm_factura`),
  KEY `ref_cli_idx` (`cod_cliente`),
  KEY `ref_formapago_idx` (`cod_formapago`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcar la base de datos para la tabla `factura`
--

INSERT INTO `factura` (`Nnm_factura`, `cod_cliente`, `Nombre_empleado`, `Fecha_facturacion`, `cod_formapago`, `total_factura`, `IVA`) VALUES
('FACT-9910966', '125', 'jose', '22/1/2013', 1, '437500', '70000');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `forma_de_pago`
--

CREATE TABLE IF NOT EXISTS `forma_de_pago` (
  `id_formapago` int(11) NOT NULL AUTO_INCREMENT,
  `Descripcion_formapago` varchar(20) NOT NULL,
  PRIMARY KEY (`id_formapago`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Volcar la base de datos para la tabla `forma_de_pago`
--

INSERT INTO `forma_de_pago` (`id_formapago`, `Descripcion_formapago`) VALUES
(1, 'EFECTIVO'),
(2, 'BONO'),
(3, 'TARJETA DE CREDITO'),
(4, 'CHEQUE');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedor`
--

CREATE TABLE IF NOT EXISTS `proveedor` (
  `No_documento` varchar(20) NOT NULL,
  `cod_tipo_documento` int(11) NOT NULL,
  `Nombre` varchar(20) NOT NULL,
  `Apellido` varchar(20) NOT NULL,
  `Nombre_comercial` varchar(20) NOT NULL,
  `direccion` varchar(20) DEFAULT NULL,
  `cod_ciudad` int(11) NOT NULL,
  `Telefono` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`No_documento`),
  KEY `ref_prov_ciudad_idx` (`cod_ciudad`),
  KEY `proveedor_ibfk_1` (`cod_tipo_documento`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcar la base de datos para la tabla `proveedor`
--

INSERT INTO `proveedor` (`No_documento`, `cod_tipo_documento`, `Nombre`, `Apellido`, `Nombre_comercial`, `direccion`, `cod_ciudad`, `Telefono`) VALUES
('00001-1', 4, 'Carlos', 'Maya', 'Estilos', 'Calle 12-12', 1, NULL),
('00002-2', 4, 'Marino', 'Burbano', 'Sports', 'Centro', 2, NULL),
('00003-A', 7, 'Paola', 'Sanchez', 'Fashion', 'Veraneras', 3, NULL),
('00004-4', 4, 'Camilo', 'Muñoz', 'Jeans&Jackets', 'Centro', 2, NULL),
('00005-F', 7, 'Marlon', 'Brandom', 'Bellas', 'Calle 34 B 12', 1, NULL),
('00006-6', 1, 'Carlos', 'sanchez diaz', 'jeans&&jeans', 'calle 45 N 23-23', 1, '8213423'),
('2222', 1, 'cccc', 'ddfff', 'ffff', 'dddd', 1, '56566'),
('43434', 7, 'fdsfdsfdsfds', 'fdsfsfds', 'fsdfdsfds', 'fsdfdsfds', 1, '543534543');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_articulo`
--

CREATE TABLE IF NOT EXISTS `tipo_articulo` (
  `id_tipoarticulo` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion_articulo` varchar(30) NOT NULL,
  PRIMARY KEY (`id_tipoarticulo`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=25 ;

--
-- Volcar la base de datos para la tabla `tipo_articulo`
--

INSERT INTO `tipo_articulo` (`id_tipoarticulo`, `descripcion_articulo`) VALUES
(19, 'ZAPATO FORMAL'),
(20, 'ZAPATO DEPORTIVO'),
(21, 'ZAPATO INFORMAL '),
(22, 'PRENDA FORMAL'),
(23, 'PRENDA DEPORTIVA'),
(24, 'PRENDA INFORMAL');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_de_documento`
--

CREATE TABLE IF NOT EXISTS `tipo_de_documento` (
  `id_tipo_documento` int(11) NOT NULL AUTO_INCREMENT,
  `Descripcion` varchar(10) NOT NULL,
  PRIMARY KEY (`id_tipo_documento`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Volcar la base de datos para la tabla `tipo_de_documento`
--

INSERT INTO `tipo_de_documento` (`id_tipo_documento`, `Descripcion`) VALUES
(1, 'CC'),
(2, 'TI'),
(3, 'RC'),
(4, 'NIT'),
(5, 'PASAPORTE'),
(6, 'CE'),
(7, 'RUT');

--
-- Filtros para las tablas descargadas (dump)
--

--
-- Filtros para la tabla `articulo`
--
ALTER TABLE `articulo`
  ADD CONSTRAINT `ref_prov_art` FOREIGN KEY (`cod_proveedor`) REFERENCES `proveedor` (`No_documento`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `ref_tipo_articulo` FOREIGN KEY (`cod_tipo_articulo`) REFERENCES `tipo_articulo` (`id_tipoarticulo`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD CONSTRAINT `ref_ciudad` FOREIGN KEY (`cod_ciudad`) REFERENCES `ciudad` (`Codigo_ciudad`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `ref_tipo_doc` FOREIGN KEY (`cod_tipo_documento`) REFERENCES `tipo_de_documento` (`id_tipo_documento`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `detalle_factura`
--
ALTER TABLE `detalle_factura`
  ADD CONSTRAINT `ref_ar_fact` FOREIGN KEY (`cod_articulo`) REFERENCES `articulo` (`id_articulo`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `ref_facturacion` FOREIGN KEY (`cod_factura`) REFERENCES `factura` (`Nnm_factura`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `devolucion`
--
ALTER TABLE `devolucion`
  ADD CONSTRAINT `ref_detallefactu` FOREIGN KEY (`cod_detallefactura`) REFERENCES `detalle_factura` (`cod_factura`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `ref_deta_art` FOREIGN KEY (`cod_detallearticulo`) REFERENCES `detalle_factura` (`cod_articulo`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `factura`
--
ALTER TABLE `factura`
  ADD CONSTRAINT `ref_cli` FOREIGN KEY (`cod_cliente`) REFERENCES `cliente` (`Documento`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `ref_formapago` FOREIGN KEY (`cod_formapago`) REFERENCES `forma_de_pago` (`id_formapago`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `proveedor`
--
ALTER TABLE `proveedor`
  ADD CONSTRAINT `proveedor_ibfk_1` FOREIGN KEY (`cod_tipo_documento`) REFERENCES `tipo_de_documento` (`id_tipo_documento`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `ref_prov_ciudad` FOREIGN KEY (`cod_ciudad`) REFERENCES `ciudad` (`Codigo_ciudad`) ON DELETE NO ACTION ON UPDATE NO ACTION;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
