CREATE TABLE `erp`.`usuarios` (`Identificador` INT NOT NULL AUTO_INCREMENT , `usuario` VARCHAR(50) NOT NULL , `contrasena` VARCHAR(50) NOT NULL , `nombrecompleto` VARCHAR(200) NOT NULL , PRIMARY KEY (`Identificador`)) ENGINE = InnoDB;

INSERT INTO `usuarios` (`Identificador`, `usuario`, `contrasena`, `nombrecompleto`) VALUES (NULL, 'jocarsa', 'jocarsa', 'Jose Vicente Carratalá');
