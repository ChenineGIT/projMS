CREATE DATABASE TimeTable;

USE TimeTable;

CREATE TABLE `class` (
  `id_class` int(5) NOT NULL,
  `name` varchar(15) NOT NULL,
  `Capacite` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `enseignematiere` (
  `id_prof` int(3) NOT NULL,
  `id_Matiere` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `etude` (
  `id_prof` int(5) NOT NULL,
  `id_groub` int(5) NOT NULL,
  `id_class` int(5) NOT NULL,
  `name_matiere` varchar(15) NOT NULL,
  `type_matiere` varchar(10) NOT NULL,
  `temps_etude` varchar(15) NOT NULL,
  `journee_etude` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `etudematiere` (
  `id_groub` int(3) NOT NULL,
  `id_Matiere` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `groub` (
  `id_groub` int(5) NOT NULL,
  `name_groub` varchar(15) NOT NULL,
  `nomber_groub` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `matiere` (
  `ID_Matiere` int(4) NOT NULL,
  `Name_Matiere` varchar(30) NOT NULL,
  `type_Matiere` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `prof` (
  `id_prof` int(5) NOT NULL,
  `name_prof` varchar(30) NOT NULL,
  `prenom_prof` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


ALTER TABLE `class`
  ADD PRIMARY KEY (`id_class`);

ALTER TABLE `enseignematiere`
  ADD PRIMARY KEY (`id_prof`,`id_Matiere`),
  ADD KEY `id_Matiere` (`id_Matiere`);

ALTER TABLE `etude`
  ADD PRIMARY KEY (`id_prof`,`id_groub`,`id_class`),
  ADD KEY `id_groub` (`id_groub`),
  ADD KEY `etude_ibfk_1` (`id_class`);

ALTER TABLE `etudematiere`
  ADD PRIMARY KEY (`id_groub`,`id_Matiere`),
  ADD KEY `id_Matiere` (`id_Matiere`);

ALTER TABLE `groub`
  ADD PRIMARY KEY (`id_groub`);

ALTER TABLE `matiere`
  ADD PRIMARY KEY (`ID_Matiere`);

ALTER TABLE `prof`
  ADD PRIMARY KEY (`id_prof`);


ALTER TABLE `enseignematiere`
  ADD CONSTRAINT `enseignematiere_ibfk_1` FOREIGN KEY (`id_Matiere`) REFERENCES `matiere` (`ID_Matiere`),
  ADD CONSTRAINT `enseignematiere_ibfk_2` FOREIGN KEY (`id_prof`) REFERENCES `prof` (`id_prof`);

ALTER TABLE `etude`
  ADD CONSTRAINT `etude_ibfk_1` FOREIGN KEY (`id_class`) REFERENCES `class` (`id_class`),
  ADD CONSTRAINT `etude_ibfk_2` FOREIGN KEY (`id_prof`) REFERENCES `prof` (`id_prof`),
  ADD CONSTRAINT `etude_ibfk_3` FOREIGN KEY (`id_groub`) REFERENCES `groub` (`id_groub`);

ALTER TABLE `etudematiere`
  ADD CONSTRAINT `etudematiere_ibfk_1` FOREIGN KEY (`id_groub`) REFERENCES `groub` (`id_groub`),
  ADD CONSTRAINT `etudematiere_ibfk_2` FOREIGN KEY (`id_Matiere`) REFERENCES `matiere` (`ID_Matiere`);
COMMIT;
