-- 1. CREACIÓN DE LA BASE DE DATOS
CREATE DATABASE IF NOT EXISTS gestion_notas;
USE gestion_notas;

-- ------------------------------------------------------------------
-- 2. CREACIÓN DE TABLAS
-- ------------------------------------------------------------------

-- Tabla: alumnos
-- Contiene la columna 'activo' para el Borrado Lógico (Etapa 7)
CREATE TABLE IF NOT EXISTS `alumnos` (
  `id_alumnos` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NOT NULL,
  `apellido` VARCHAR(255) NOT NULL,
  `dni` VARCHAR(20) NOT NULL,
  `activo` TINYINT(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_alumnos`),
  UNIQUE KEY `dni_UNIQUE` (`dni`)
);

-- Tabla: materias (Catálogo)
CREATE TABLE IF NOT EXISTS `materias` (
  `id_materias` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id_materias`)
);

-- Tabla: anios (Catálogo)
CREATE TABLE IF NOT EXISTS `anios` (
  `id_anios` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id_anios`)
);

-- Tabla: estados (Catálogo)
CREATE TABLE IF NOT EXISTS `estados` (
  `id_estados` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id_estados`)
);

-- Tabla: notas
-- Contiene las llaves foráneas a todas las otras tablas
CREATE TABLE IF NOT EXISTS `notas` (
  `id_notas` INT NOT NULL AUTO_INCREMENT,
  `id_alumnos` INT NOT NULL,
  `id_materias` INT NOT NULL,
  `nota_final` DECIMAL(4,2) NOT NULL,
  `id_anios` INT NOT NULL,
  `id_estados` INT NOT NULL,
  `fecha` DATE NULL,
  PRIMARY KEY (`id_notas`),
  
  -- Definición de las "correas" (Llaves Foráneas)
  INDEX `fk_notas_alumnos_idx` (`id_alumnos` ASC),
  INDEX `fk_notas_materias_idx` (`id_materias` ASC),
  INDEX `fk_notas_anios_idx` (`id_anios` ASC),
  INDEX `fk_notas_estados_idx` (`id_estados` ASC),
  
  CONSTRAINT `fk_notas_alumnos`
    FOREIGN KEY (`id_alumnos`)
    REFERENCES `alumnos` (`id_alumnos`)
    ON DELETE CASCADE, -- (Arreglo de la Etapa 7)
    
  CONSTRAINT `fk_notas_materias`
    FOREIGN KEY (`id_materias`)
    REFERENCES `materias` (`id_materias`),
    
  CONSTRAINT `fk_notas_anios`
    FOREIGN KEY (`id_anios`)
    REFERENCES `anios` (`id_anios`),
    
  CONSTRAINT `fk_notas_estados`
    FOREIGN KEY (`id_estados`)
    REFERENCES `estados` (`id_estados`)
);

-- ------------------------------------------------------------------
-- 3. POBLACIÓN DE TABLAS DE CATÁLOGO
-- ------------------------------------------------------------------

-- Se vacían por si el script se corre más de una vez
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE materias;
TRUNCATE TABLE anios;
TRUNCATE TABLE estados;
SET FOREIGN_KEY_CHECKS = 1;

-- Poblar 'materias'
INSERT INTO materias (descripcion) VALUES
('Matemática Aplicada'),
('Lenguaje II'),
('POO'),
('Análisis de Sistemas'),
('Análisis Matemático'),
('Estadística y Probabilidad'),
('Taller de Redes'),
('Matemática Financiera');

-- Poblar 'estados' (con la última lógica de negocio)
INSERT INTO estados (descripcion) VALUES
('Promocionado'),
('Regular'),
('Recursante');

-- Poblar 'anios' (hasta 3er Año)
INSERT INTO anios (descripcion) VALUES
('1er Año'),
('2do Año'),
('3er Año');


-- ------------------------------------------------------------------
-- FIN DEL SCRIPT
-- ------------------------------------------------------------------

SELECT 'Script de creación de BD completado.' AS Resultado;