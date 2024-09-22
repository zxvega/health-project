CREATE TABLE Medico (
	idMedico INT IDENTITY PRIMARY KEY,
    DNI VARCHAR(9) UNIQUE,					
    nombres VARCHAR(100) NOT NULL,	
    fechaNacimiento DATE NOT NULL,         
	apellidoPaterno VARCHAR(100) NOT NULL,
	apellidoMaterno VARCHAR(100) NOT NULL,		
);

CREATE TABLE Hospital (
	idHospital INT IDENTITY PRIMARY KEY,
    codigoHospital VARCHAR(255) NOT NULL,		
    nombre VARCHAR(255) NOT NULL,				
    ciudad VARCHAR(255) NOT NULL,				
    telefono VARCHAR(15),						
);

-- IMÁGENES DIAGNOSTICAS, LABORATORIO, EMERGENCIAS, INTERNACIÓN, UTI ADULTO, CONSULTORIO

CREATE TABLE Servicio (
	idServicio INT IDENTITY PRIMARY KEY,
    nombreCompleto VARCHAR(200) NOT NULL,
    comentario VARCHAR(255) NULL         
);


CREATE TABLE HospitalServicio (
    idHospitalServicio INT IDENTITY PRIMARY KEY,
    idHospital INT NOT NULL,                   
    idServicio INT NOT NULL,                   
    fechaInicio DATE NOT NULL,                 
    fechaFin DATE,                             
    FOREIGN KEY (idHospital) REFERENCES Hospital(idHospital),
    FOREIGN KEY (idServicio) REFERENCES Servicio(idServicio)
);

/* Con una consulta se puede obtener el director en curso de un hospital en base a la fecha*/

CREATE TABLE DirectorHospital (
    idDirectorHospital INT IDENTITY PRIMARY KEY,
    idMedico INT NOT NULL,                      
    idHospital INT NOT NULL,                    
    fechaInicio DATE NOT NULL,                  
    fechaFin DATE,                              
    FOREIGN KEY (idMedico) REFERENCES Medico(idMedico),
    FOREIGN KEY (idHospital) REFERENCES Hospital(idHospital)
);

/* Filtrando por hospital tendriamos el plantel medico */

CREATE TABLE MedicoHospitalServicio (
    idMedicoHospitalServicio INT IDENTITY PRIMARY KEY,
    idMedico INT NOT NULL,                      
    idHospital INT NOT NULL,                    
    idServicio INT NOT NULL,                    
    fechaInicio DATE NOT NULL,                  
    fechaFin DATE,                              
    FOREIGN KEY (idMedico) REFERENCES Medico(idMedico),
    FOREIGN KEY (idHospital) REFERENCES Hospital(idHospital),
    FOREIGN KEY (idServicio) REFERENCES Servicio(idServicio)
);


CREATE TABLE Habitacion (
	idHabitacion INT IDENTITY PRIMARY KEY,
    nombreCompleto VARCHAR(200) NOT NULL, 
	idHospitalServicio INT NOT NULL,
	FOREIGN KEY (idHabitacion) REFERENCES HospitalServicio(idHospitalServicio)
);

CREATE TABLE Cama (
	idCama INT IDENTITY PRIMARY KEY,
    nombreCompleto VARCHAR(200) NOT NULL,
    idHabitacion INT NOT NULL,
	estaOcupada BIT DEFAULT 0,
	FOREIGN KEY (idHabitacion) REFERENCES Habitacion(idHabitacion)
);


CREATE TABLE Paciente (
    codHist  INT IDENTITY(100000, 1) PRIMARY KEY,              
    DNI VARCHAR(9) NOT NULL,             
    apellidosNombre VARCHAR(100) NOT NULL, 
    fechaNacimiento DATE NOT NULL,          
    numSeguridadSocial VARCHAR(15) NOT NULL, 
    otrosDatos VARCHAR(255) NULL,
	sexo VARCHAR(1) NULL, 		
);

-- Tabla Visita 
-- TODO: Mejorar respecto al movimiento del paciente entre servicios 
CREATE TABLE Visita (
    idVisita INT IDENTITY PRIMARY KEY,      
    fecha DATE NOT NULL,                    
    hora TIME NOT NULL,                     
    idHospital INT NOT NULL,               
    idServicio INT NOT NULL,       
    idMedico INT NOT NULL,        
    codHist INT NOT NULL,                   
    diagnostico VARCHAR(255) NOT NULL,     
    tratamiento VARCHAR(255) NOT NULL,     
    esIngreso BIT DEFAULT 0,                
    idCama INT NULL,                   
    fechaAlta DATE NULL,                    -- Fecha en la que fue dado de alta (si aplica)
    FOREIGN KEY (idHospital) REFERENCES Hospital(idHospital),
    FOREIGN KEY (idServicio) REFERENCES Servicio(idServicio),
    FOREIGN KEY (idMedico) REFERENCES Medico(idMedico),
	FOREIGN KEY (idCama) REFERENCES Cama(idCama),
    FOREIGN KEY (codHist) REFERENCES Paciente(codHist)
);
