-- Datos de prueba para el sistema de gestión de notas

-- Insertar años académicos
INSERT INTO anios (id_anios, descripcion) VALUES (1, 2023);
INSERT INTO anios (id_anios, descripcion) VALUES (2, 2024);
INSERT INTO anios (id_anios, descripcion) VALUES (3, 2025);

-- Insertar estados
INSERT INTO estados (id_estados, descripcion) VALUES (1, 'Aprobado');
INSERT INTO estados (id_estados, descripcion) VALUES (2, 'Desaprobado');
INSERT INTO estados (id_estados, descripcion) VALUES (3, 'Pendiente');
INSERT INTO estados (id_estados, descripcion) VALUES (4, 'Ausente');

-- Insertar materias
INSERT INTO materias (id_materias, descripcion, condicion) VALUES (1, 'Matemática', 1);
INSERT INTO materias (id_materias, descripcion, condicion) VALUES (2, 'Lengua y Literatura', 1);
INSERT INTO materias (id_materias, descripcion, condicion) VALUES (3, 'Programación Orientada a Objetos', 1);
INSERT INTO materias (id_materias, descripcion, condicion) VALUES (4, 'Base de Datos', 1);
INSERT INTO materias (id_materias, descripcion, condicion) VALUES (5, 'Inglés Técnico', 1);
INSERT INTO materias (id_materias, descripcion, condicion) VALUES (6, 'Sistemas Operativos', 1);
INSERT INTO materias (id_materias, descripcion, condicion) VALUES (7, 'Redes y Comunicaciones', 1);
INSERT INTO materias (id_materias, descripcion, condicion) VALUES (8, 'Desarrollo Web', 1);

-- Insertar alumnos de ejemplo
INSERT INTO alumnos (id_alumnos, nombre, apellido, dni, condicion) 
VALUES (1, 'Juan', 'Pérez', 12345678, 1);

INSERT INTO alumnos (id_alumnos, nombre, apellido, dni, condicion) 
VALUES (2, 'María', 'González', 23456789, 1);

INSERT INTO alumnos (id_alumnos, nombre, apellido, dni, condicion) 
VALUES (3, 'Carlos', 'Rodríguez', 34567890, 1);

INSERT INTO alumnos (id_alumnos, nombre, apellido, dni, condicion) 
VALUES (4, 'Ana', 'Martínez', 45678901, 1);

INSERT INTO alumnos (id_alumnos, nombre, apellido, dni, condicion) 
VALUES (5, 'Luis', 'Fernández', 56789012, 1);

-- Insertar algunas notas de ejemplo
INSERT INTO notas (id_notas, id_alumnos, id_materias, nota_final, id_anios, id_estados, condicion)
VALUES (1, 1, 1, 8.5, 2, 1, 1);

INSERT INTO notas (id_notas, id_alumnos, id_materias, nota_final, id_anios, id_estados, condicion)
VALUES (2, 1, 3, 9.0, 2, 1, 1);

INSERT INTO notas (id_notas, id_alumnos, id_materias, nota_final, id_anios, id_estados, condicion)
VALUES (3, 2, 1, 7.5, 2, 1, 1);

INSERT INTO notas (id_notas, id_alumnos, id_materias, nota_final, id_anios, id_estados, condicion)
VALUES (4, 2, 4, 8.0, 2, 1, 1);

INSERT INTO notas (id_notas, id_alumnos, id_materias, nota_final, id_anios, id_estados, condicion)
VALUES (5, 3, 3, 6.5, 2, 1, 1);
