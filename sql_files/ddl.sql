create table if not exists cliente
(
    curp          char(18)     not null
        constraint cliente_pkey
            primary key
        constraint cliente_curp_key
            unique
        constraint cliente_curp_check
            check (char_length(curp) = 18),
    nombre        varchar(100)
        constraint cliente_nombre_check
            check ((nombre)::text <> ''::text),
    a_paterno     varchar(100)
        constraint cliente_a_paterno_check
            check ((a_paterno)::text <> ''::text),
    a_materno     varchar(100)
        constraint cliente_a_materno_check
            check ((a_materno)::text <> ''::text),
    fotografia    varchar(100)
        constraint cliente_fotografia_key
            unique
        constraint cliente_fotografia_check
            check ((fotografia)::text <> ''::text),
    email         varchar(100) not null
        constraint cliente_email_check
            check ((email)::text ~~ '%@%.%'::text),
    tel_celular   bigint       not null
        constraint cliente_tel_celular_key
            unique,
    tel_casa      bigint       not null
        constraint cliente_tel_casa_key
            unique,
    estado        varchar(100) not null
        constraint cliente_estado_check
            check ((estado)::text <> ''::text),
    municipio     varchar(100) not null
        constraint cliente_municipio_check
            check ((municipio)::text <> ''::text),
    colonia       varchar(100) not null
        constraint cliente_colonia_check
            check ((colonia)::text <> ''::text),
    cp            integer      not null
        constraint cliente_cp_check
            check ((cp >= 0) AND (cp <= 99999)),
    calle_num     varchar(100) not null
        constraint cliente_calle_num_check
            check ((calle_num)::text <> ''::text),
    facultad      varchar(100)
        constraint cliente_facultad_check
            check ((facultad)::text <> ''::text),
    instituto     varchar(100)
        constraint cliente_instituto_check
            check ((instituto)::text <> ''::text),
    unidad        varchar(100)
        constraint cliente_unidad_check
            check ((unidad)::text <> ''::text),
    es_alumno     boolean,
    es_academico  boolean,
    es_trabajador boolean
);

comment on table cliente is 'Tabla que contiene los clientes que contraten el servicio de taxi de la asociacion de taxis "El Pumita"';

comment on constraint cliente_pkey on cliente is 'La llave primaria de la tabla cliente';

comment on column cliente.nombre is 'Nombre del cliente';

comment on column cliente.a_paterno is 'Apellido paterno del cliente';

comment on column cliente.a_materno is 'Apellido materno del cliente';

comment on column cliente.fotografia is 'Ruta de la fotografia';

comment on column cliente.email is 'Email del cliente';

comment on column cliente.tel_celular is 'Telefono celular del cliente';

comment on column cliente.tel_casa is 'Telefono de casa del cliente';

comment on column cliente.estado is 'Estado donde vive el cliente';

comment on column cliente.municipio is 'Municipio donde vive el cliente';

comment on column cliente.colonia is 'Colonia donde vive el cliente';

comment on column cliente.cp is 'Codigo postal del lugar donde vive el cliente';

comment on column cliente.calle_num is 'Calle del lugar donde vive el cliente';

comment on column cliente.facultad is 'Facultad a la que pertenece el cliente';

comment on column cliente.instituto is 'Instituto a la que pertenece el cliente';

comment on column cliente.unidad is 'Instituto a la que pertenece el cliente';

comment on column cliente.es_alumno is 'Nos dice si es alumno';

comment on column cliente.es_academico is 'Nos dice si es academico';

comment on column cliente.es_trabajador is 'Nos dice si es trabajador';

alter table cliente
    owner to postgres;

create table if not exists socio
(
    id_socio     varchar(100) not null
        constraint socio_pkey
            primary key
        constraint socio_id_socio_key
            unique
        constraint socio_id_socio_check
            check ((id_socio)::text <> ''::text),
    nombre       varchar(100)
        constraint socio_nombre_check
            check ((nombre)::text <> ''::text),
    a_paterno    varchar(100)
        constraint socio_a_paterno_check
            check ((a_paterno)::text <> ''::text),
    a_materno    varchar(100)
        constraint socio_a_materno_check
            check ((a_materno)::text <> ''::text),
    fotografia   varchar(100) not null
        constraint socio_fotografia_key
            unique
        constraint socio_fotografia_check
            check ((fotografia)::text <> ''::text),
    tel_celular  bigint       not null
        constraint socio_tel_celular_key
            unique,
    email        varchar(100) not null
        constraint socio_email_check
            check ((email)::text ~~ '%@%.%'::text),
    ingreso      date         not null,
    egreso       date,
    estado       varchar(100) not null
        constraint socio_estado_check
            check ((estado)::text <> ''::text),
    municipio    varchar(100) not null
        constraint socio_municipio_check
            check ((municipio)::text <> ''::text),
    colonia      varchar(100) not null
        constraint socio_colonia_check
            check ((colonia)::text <> ''::text),
    cp           integer      not null
        constraint socio_cp_check
            check ((cp >= 0) AND (cp <= 99999)),
    calle_num    varchar(100) not null
        constraint socio_calle_num_check
            check ((calle_num)::text <> ''::text),
    num_licencia char(9)      not null
        constraint socio_num_licencia_check
            check (num_licencia <> ''::bpchar),
    rfc          char(14)     not null
        constraint socio_rfc_key
            unique
        constraint socio_rfc_check
            check (rfc <> ''::bpchar),
    es_duenio    boolean,
    es_chofer    boolean
);

comment on table socio is 'Tabla que contiene los socios de la asociacion de taxis "El Pumita"';

comment on constraint socio_pkey on socio is 'La llave primaria de la tabla socio';

comment on column socio.nombre is 'Nombre del socio';

comment on column socio.a_paterno is 'Apellido paterno del socio';

comment on column socio.a_materno is 'Apellido materno del socio';

comment on column socio.fotografia is 'Ruta de la fotografia';

comment on column socio.tel_celular is 'Telefono celular del socio';

comment on column socio.email is 'Email del cliente';

comment on column socio.ingreso is 'Fecha de inicio de contrato del socio';

comment on column socio.egreso is 'Fecha de fin del contrato del socio';

comment on column socio.estado is 'Estado donde vive el socio';

comment on column socio.municipio is 'Municipio donde vive el socio';

comment on column socio.colonia is 'Colonia donde vive el socio';

comment on column socio.cp is 'Codigo postal del lugar donde vive el socio';

comment on column socio.calle_num is 'Calle del lugar donde vive el socio';

comment on column socio.rfc is 'Registro Federal del Contribuyente del socio';

comment on column socio.es_duenio is 'Nos dice si es duenio';

comment on column socio.es_chofer is 'Nos dice si es chofer';

alter table socio
    owner to postgres;

create table if not exists vehiculo
(
    num_economico   varchar(100) not null
        constraint vehiculo_pkey
            primary key
        constraint vehiculo_num_economico_key
            unique
        constraint vehiculo_num_economico_check
            check ((num_economico)::text <> ''::text),
    id_socio        varchar(100) not null
        constraint vehiculo_fkey
            references socio
        constraint vehiculo_id_socio_check
            check ((id_socio)::text <> ''::text),
    anio            integer      not null,
    marca           varchar(100) not null
        constraint vehiculo_marca_check
            check ((marca)::text <> ''::text),
    modelo          varchar(100) not null
        constraint vehiculo_modelo_check
            check ((modelo)::text <> ''::text),
    tipo_conduccion varchar(100) not null
        constraint vehiculo_tipo_conduccion_check
            check ((tipo_conduccion)::text <> ''::text),
    num_cilindros   integer      not null,
    pasajeros       integer      not null,
    puertas         integer      not null,
    combustible     varchar(100) not null
        constraint vehiculo_combustible_check
            check ((combustible)::text <> ''::text),
    refaccion       boolean,
    aseguradora     varchar(100) not null
        constraint vehiculo_aseguradora_check
            check ((aseguradora)::text <> ''::text),
    tipo_seg        varchar(100) not null
        constraint vehiculo_tipo_seg_check
            check ((tipo_seg)::text <> ''::text),
    vigencia_seg    date,
    activo          boolean,
    razon           varchar(100) not null
        constraint vehiculo_razon_check
            check ((razon)::text <> ''::text)
);

comment on table vehiculo is 'Tabla de los vehiculos utilizados en el servicio de taxi de la asociacion "El Pumita"';

comment on constraint vehiculo_pkey on vehiculo is 'La llave primaria de la tabla vehiculo';

comment on constraint vehiculo_fkey on vehiculo is 'LLave Foranea de la tabla vehiculo que hace referencia al id_socio de socio';

comment on column vehiculo.anio is 'El anio del vehiculo';

comment on column vehiculo.marca is 'Marca del vehiculo';

comment on column vehiculo.modelo is 'Modelo del vehiculo';

comment on column vehiculo.tipo_conduccion is 'El tipo de conduccion del vehiculo';

comment on column vehiculo.num_cilindros is 'Numero de cilindros del del vehiculo';

comment on column vehiculo.pasajeros is 'Cantidad de pasajeros soportados por el vehiculo';

comment on column vehiculo.puertas is 'Numero de puertas que posee el vehiculo';

comment on column vehiculo.combustible is 'Tipo de combustible que utiliza el vehiculo';

comment on column vehiculo.refaccion is 'Nos dice si el vehiculo tiene o no refacccion';

comment on column vehiculo.aseguradora is 'La aseguradora del vehiculo';

comment on column vehiculo.tipo_seg is 'Tipo de seguto del vehiculo';

comment on column vehiculo.vigencia_seg is 'Vigencia del seguro del vehiculo';

comment on column vehiculo.activo is 'Nos dice si el vehiculo esta activo o no';

comment on column vehiculo.razon is 'Razon por la que el vehiculo no esta activo';

alter table vehiculo
    owner to postgres;

create table if not exists viaje
(
    id_viaje      varchar(100) not null
        constraint viaje_pkey
            primary key
        constraint viaje_id_viaje_key
            unique,
    id_socio      varchar(100) not null
        constraint viaje_fkey1
            references socio
        constraint viaje_id_socio_check
            check ((id_socio)::text <> ''::text),
    num_economico varchar(100) not null
        constraint viaje_fkey2
            references vehiculo
        constraint viaje_num_economico_check
            check ((num_economico)::text <> ''::text),
    distancia     real         not null,
    tiempo        integer      not null,
    fecha         date         not null
);

comment on table viaje is 'Tabla de los viajes realizados por los clientes que contraten el servicio de taxi de la asociacion "El Pumita"';

comment on constraint viaje_pkey on viaje is 'La llave primaria de la tabla viaje';

comment on constraint viaje_fkey1 on viaje is 'LLave Foranea de la tabla viaje que hace referencia al id_socio de socio';

comment on constraint viaje_fkey2 on viaje is 'LLave Foranea de la tabla viaje que hace referencia al num_economico de vehiculo';

comment on column viaje.distancia is 'Distancia recorrida en el viaje hecha por el taxi de la asociacion "El Pumita"';

comment on column viaje.tiempo is 'Tiempo de duracion del viaje hecho por el taxi de la asociacion "El Pumita"';

comment on column viaje.fecha is 'Fecha en la que se realizo el viaje hecho por el taxi de la asociacion "El Pumita"';

alter table viaje
    owner to postgres;

create table if not exists infraccion
(
    id_infraccion varchar(100) not null
        constraint infraccion_pkey
            primary key
        constraint infraccion_id_infraccion_check
            check ((id_infraccion)::text <> ''::text),
    id_socio      varchar(100) not null
        constraint infraccion_fkey1
            references socio
        constraint infraccion_id_socio_check
            check ((id_socio)::text <> ''::text),
    num_economico varchar(100) not null
        constraint infraccion_fkey2
            references vehiculo
        constraint infraccion_num_economico_check
            check ((num_economico)::text <> ''::text),
    monto_pagar   money,
    agente        varchar(100) not null
        constraint infraccion_agente_check
            check ((agente)::text <> ''::text),
    fecha         date,
    hora          time,
    municipio     varchar(100) not null
        constraint infraccion_municipio_check
            check ((municipio)::text <> ''::text),
    cp            integer      not null
        constraint infraccion_cp_check
            check ((cp >= 0) AND (cp <= 99999)),
    calle         varchar(100) not null
        constraint infraccion_calle_check
            check ((calle)::text <> ''::text)
);

comment on table infraccion is 'Tabla que contiene las infracciones de los choferes dela asociacion de taxis "El Pumita"';

comment on constraint infraccion_pkey on infraccion is 'La llave primaria de la tabla infraccion';

comment on constraint infraccion_fkey1 on infraccion is 'LLave Foranea de la tabla infraccion que hace referencia al id_socio de socio';

comment on constraint infraccion_fkey2 on infraccion is 'LLave Foranea de la tabla infraccion que hace referencia al num_economico de vehiculo';

comment on column infraccion.monto_pagar is 'Dinero que tiene que pagar el chofer por cometer la infraccion';

comment on column infraccion.agente is 'Agente que puso la infraccion';

comment on column infraccion.fecha is 'Fecha de la infraccion';

comment on column infraccion.hora is 'Hora de la infraccion';

comment on column infraccion.municipio is 'Municipio donde se cometio la infraccion';

comment on column infraccion.cp is 'Codigo postal del lugar donde se cometio la infraccion';

comment on column infraccion.calle is 'Calle donde se cometio la infraccion';

alter table infraccion
    owner to postgres;

create table if not exists programar
(
    curp      char(18)     not null
        constraint programar_fkey1
            references cliente
        constraint programar_curp_check
            check (char_length(curp) = 18),
    id_viaje  varchar(100) not null
        constraint programar_id_viaje_key
            unique
        constraint programar_fkey2
            references viaje
        constraint programar_id_viaje_check
            check ((id_viaje)::text <> ''::text),
    h_entrada time,
    h_salida  time,
    redondo   boolean
);

comment on table programar is 'Tabla de los viajes programados por los clientes que contraten el servicio de taxi de la asociacion "El Pumita"';

comment on constraint programar_fkey1 on programar is 'LLave Foranea de la tabla programar que hace referencia al curp de cliente';

comment on constraint programar_fkey2 on programar is 'LLave Foranea de la tabla programar que hace referencia al id_viaje de viaje';

comment on column programar.h_entrada is 'La hora de entrada de los clientes';

comment on column programar.h_salida is 'La hora de salida de los clientes';

comment on column programar.redondo is 'Nos dice si el viaje sera de ida y vuelta';

alter table programar
    owner to postgres;

create table if not exists abordar
(
    curp     char(18)     not null
        constraint abordar_fkey1
            references cliente
        constraint abordar_curp_check
            check (char_length(curp) = 18),
    id_viaje varchar(100) not null
        constraint abordar_fkey2
            references viaje
        constraint abordar_id_viaje_check
            check ((id_viaje)::text <> ''::text),
    origen   varchar(100) not null
        constraint abordar_origen_check
            check ((origen)::text <> ''::text),
    destino  varchar(100) not null
        constraint abordar_destino_check
            check ((destino)::text <> ''::text)
);

comment on table abordar is 'Tabla del aborde de los clientes que contraten el servicio de taxi de la asociacion "El Pumita"';

comment on constraint abordar_fkey1 on abordar is 'LLave Foranea de la tabla abordar que hace referencia al curp de cliente';

comment on constraint abordar_fkey2 on abordar is 'LLave Foranea de la tabla abordar que hace referencia al id_viaje de viaje';

comment on column abordar.origen is 'Lugar de origen del viaje';

comment on column abordar.destino is 'Lugar de destino del viaje';

alter table abordar
    owner to postgres;


