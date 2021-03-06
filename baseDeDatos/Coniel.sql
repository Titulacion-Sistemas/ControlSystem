--
-- PostgreSQL database dump
--

-- Dumped from database version 9.1.10
-- Dumped by pg_dump version 9.3.1
-- Started on 2014-11-24 21:07:00

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 262 (class 3079 OID 11639)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2634 (class 0 OID 0)
-- Dependencies: 262
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 161 (class 1259 OID 27513)
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- TOC entry 162 (class 1259 OID 27516)
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- TOC entry 2635 (class 0 OID 0)
-- Dependencies: 162
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- TOC entry 163 (class 1259 OID 27518)
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- TOC entry 164 (class 1259 OID 27521)
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- TOC entry 2636 (class 0 OID 0)
-- Dependencies: 164
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- TOC entry 165 (class 1259 OID 27523)
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- TOC entry 166 (class 1259 OID 27526)
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- TOC entry 2637 (class 0 OID 0)
-- Dependencies: 166
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- TOC entry 167 (class 1259 OID 27528)
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone NOT NULL,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    sesion_sico character varying(2)
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- TOC entry 168 (class 1259 OID 27531)
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- TOC entry 169 (class 1259 OID 27534)
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO postgres;

--
-- TOC entry 2638 (class 0 OID 0)
-- Dependencies: 169
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- TOC entry 170 (class 1259 OID 27536)
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO postgres;

--
-- TOC entry 2639 (class 0 OID 0)
-- Dependencies: 170
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- TOC entry 171 (class 1259 OID 27538)
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- TOC entry 172 (class 1259 OID 27541)
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- TOC entry 2640 (class 0 OID 0)
-- Dependencies: 172
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- TOC entry 173 (class 1259 OID 27543)
-- Name: auth_user_usuario_sico; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_user_usuario_sico (
    id integer NOT NULL,
    user_id integer NOT NULL,
    usuariosico_id integer NOT NULL
);


ALTER TABLE public.auth_user_usuario_sico OWNER TO postgres;

--
-- TOC entry 174 (class 1259 OID 27546)
-- Name: auth_user_usuario_sico_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_usuario_sico_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_usuario_sico_id_seq OWNER TO postgres;

--
-- TOC entry 2641 (class 0 OID 0)
-- Dependencies: 174
-- Name: auth_user_usuario_sico_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_usuario_sico_id_seq OWNED BY auth_user_usuario_sico.id;


--
-- TOC entry 175 (class 1259 OID 27548)
-- Name: busquedas_vitacorabusquedas; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE busquedas_vitacorabusquedas (
    id integer NOT NULL,
    "tipoBusq" character varying(1) NOT NULL,
    "fechaHora" timestamp with time zone NOT NULL,
    consulta character varying(20) NOT NULL,
    usuario_id integer NOT NULL,
    "estadoRetorno" boolean NOT NULL
);


ALTER TABLE public.busquedas_vitacorabusquedas OWNER TO postgres;

--
-- TOC entry 176 (class 1259 OID 27551)
-- Name: busquedas_vitacorabusquedas_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE busquedas_vitacorabusquedas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.busquedas_vitacorabusquedas_id_seq OWNER TO postgres;

--
-- TOC entry 2642 (class 0 OID 0)
-- Dependencies: 176
-- Name: busquedas_vitacorabusquedas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE busquedas_vitacorabusquedas_id_seq OWNED BY busquedas_vitacorabusquedas.id;


--
-- TOC entry 177 (class 1259 OID 27553)
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    content_type_id integer,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- TOC entry 178 (class 1259 OID 27560)
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- TOC entry 2643 (class 0 OID 0)
-- Dependencies: 178
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- TOC entry 179 (class 1259 OID 27562)
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- TOC entry 180 (class 1259 OID 27565)
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- TOC entry 2644 (class 0 OID 0)
-- Dependencies: 180
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- TOC entry 181 (class 1259 OID 27567)
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- TOC entry 182 (class 1259 OID 27573)
-- Name: ingresos_actividad; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_actividad (
    id integer NOT NULL,
    "numeroDeSolicitud" character varying(10) NOT NULL,
    cliente_id integer NOT NULL,
    "tipoDeConstruccion_id" integer NOT NULL,
    "materialDeRed" character varying(5),
    instalador_id integer NOT NULL,
    "ubicacionDelMedidor_id" integer NOT NULL,
    "claseRed_id" character varying(1) NOT NULL,
    "nivelSocieconomico_id" character varying(2),
    "calibreDeLaRed_id" integer NOT NULL,
    "estadoDeLaInstalacion_id" integer NOT NULL,
    "tipoDeAcometidaRed_id" character varying(2) NOT NULL,
    "fechaDeActividad" timestamp with time zone NOT NULL,
    "usoDeEnergia_id" character varying(2) NOT NULL,
    "usoEspecificoDelInmueble_id" integer NOT NULL,
    "formaDeConexion_id" integer NOT NULL,
    demanda_id integer NOT NULL,
    "motivoDeSolicitud_id" integer NOT NULL,
    "tipoDeSolicitud_id" integer NOT NULL
);


ALTER TABLE public.ingresos_actividad OWNER TO postgres;

--
-- TOC entry 183 (class 1259 OID 27576)
-- Name: ingresos_actividad_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ingresos_actividad_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ingresos_actividad_id_seq OWNER TO postgres;

--
-- TOC entry 2645 (class 0 OID 0)
-- Dependencies: 183
-- Name: ingresos_actividad_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE ingresos_actividad_id_seq OWNED BY ingresos_actividad.id;


--
-- TOC entry 184 (class 1259 OID 27578)
-- Name: ingresos_calibredelared; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_calibredelared (
    id smallint NOT NULL,
    descripcion character varying(25) NOT NULL,
    CONSTRAINT ingresos_calibredelared_id_check CHECK ((id >= 0))
);


ALTER TABLE public.ingresos_calibredelared OWNER TO postgres;

--
-- TOC entry 185 (class 1259 OID 27582)
-- Name: ingresos_calle; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_calle (
    id integer NOT NULL,
    descripcion1 character varying(40) NOT NULL,
    "tipoDeCalle_id" character varying(2),
    "codigoDeCalle" character varying(6),
    descripcion2 character varying(40)
);


ALTER TABLE public.ingresos_calle OWNER TO postgres;

--
-- TOC entry 186 (class 1259 OID 27585)
-- Name: ingresos_calle_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ingresos_calle_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ingresos_calle_id_seq OWNER TO postgres;

--
-- TOC entry 2646 (class 0 OID 0)
-- Dependencies: 186
-- Name: ingresos_calle_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE ingresos_calle_id_seq OWNED BY ingresos_calle.id;


--
-- TOC entry 187 (class 1259 OID 27587)
-- Name: ingresos_canton; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_canton (
    id integer NOT NULL,
    num smallint NOT NULL,
    descripcion character varying(30),
    provincia_id integer NOT NULL,
    CONSTRAINT ingresos_canton_num_check CHECK ((num >= 0))
);


ALTER TABLE public.ingresos_canton OWNER TO postgres;

--
-- TOC entry 188 (class 1259 OID 27591)
-- Name: ingresos_canton_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ingresos_canton_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ingresos_canton_id_seq OWNER TO postgres;

--
-- TOC entry 2647 (class 0 OID 0)
-- Dependencies: 188
-- Name: ingresos_canton_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE ingresos_canton_id_seq OWNED BY ingresos_canton.id;


--
-- TOC entry 189 (class 1259 OID 27593)
-- Name: ingresos_caserio; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_caserio (
    id integer NOT NULL,
    descripcion character varying(50) NOT NULL
);


ALTER TABLE public.ingresos_caserio OWNER TO postgres;

--
-- TOC entry 190 (class 1259 OID 27596)
-- Name: ingresos_caserio_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ingresos_caserio_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ingresos_caserio_id_seq OWNER TO postgres;

--
-- TOC entry 2648 (class 0 OID 0)
-- Dependencies: 190
-- Name: ingresos_caserio_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE ingresos_caserio_id_seq OWNED BY ingresos_caserio.id;


--
-- TOC entry 191 (class 1259 OID 27598)
-- Name: ingresos_clasered; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_clasered (
    id character varying(1) NOT NULL,
    descripcion character varying(25) NOT NULL
);


ALTER TABLE public.ingresos_clasered OWNER TO postgres;

--
-- TOC entry 192 (class 1259 OID 27601)
-- Name: ingresos_cliente; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_cliente (
    id integer NOT NULL,
    ci_ruc character varying(13) NOT NULL,
    cuenta character varying(7) NOT NULL,
    nombre character varying(50) NOT NULL,
    deuda numeric(12,2) NOT NULL,
    meses smallint NOT NULL,
    geocodigo_id integer NOT NULL,
    "ubicacionGeografica_id" integer NOT NULL,
    tipo character varying(1) NOT NULL,
    estado character varying(20) NOT NULL,
    telefono character varying(10),
    CONSTRAINT ingresos_cliente_meses_check CHECK ((meses >= 0))
);


ALTER TABLE public.ingresos_cliente OWNER TO postgres;

--
-- TOC entry 193 (class 1259 OID 27605)
-- Name: ingresos_cliente_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ingresos_cliente_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ingresos_cliente_id_seq OWNER TO postgres;

--
-- TOC entry 2649 (class 0 OID 0)
-- Dependencies: 193
-- Name: ingresos_cliente_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE ingresos_cliente_id_seq OWNED BY ingresos_cliente.id;


--
-- TOC entry 194 (class 1259 OID 27607)
-- Name: ingresos_cuadrilla; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_cuadrilla (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL,
    observacion character varying(50)
);


ALTER TABLE public.ingresos_cuadrilla OWNER TO postgres;

--
-- TOC entry 195 (class 1259 OID 27610)
-- Name: ingresos_cuadrilla_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ingresos_cuadrilla_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ingresos_cuadrilla_id_seq OWNER TO postgres;

--
-- TOC entry 2650 (class 0 OID 0)
-- Dependencies: 195
-- Name: ingresos_cuadrilla_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE ingresos_cuadrilla_id_seq OWNED BY ingresos_cuadrilla.id;


--
-- TOC entry 196 (class 1259 OID 27612)
-- Name: ingresos_demanda; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_demanda (
    id smallint NOT NULL,
    descripcion character varying(40) NOT NULL,
    CONSTRAINT ingresos_demanda_id_check CHECK ((id >= 0))
);


ALTER TABLE public.ingresos_demanda OWNER TO postgres;

--
-- TOC entry 197 (class 1259 OID 27616)
-- Name: ingresos_detalleclientemedidor; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_detalleclientemedidor (
    id integer NOT NULL,
    lectura_instalacion numeric(8,2) NOT NULL,
    lectura_desinstalacion numeric(8,2) NOT NULL,
    fecha_instalacion date NOT NULL,
    fecha_desinstalacion date NOT NULL,
    medidor_id integer NOT NULL,
    cliente_id integer NOT NULL,
    observacion character varying(50)
);


ALTER TABLE public.ingresos_detalleclientemedidor OWNER TO postgres;

--
-- TOC entry 198 (class 1259 OID 27619)
-- Name: ingresos_detalleclientemedidor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ingresos_detalleclientemedidor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ingresos_detalleclientemedidor_id_seq OWNER TO postgres;

--
-- TOC entry 2651 (class 0 OID 0)
-- Dependencies: 198
-- Name: ingresos_detalleclientemedidor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE ingresos_detalleclientemedidor_id_seq OWNED BY ingresos_detalleclientemedidor.id;


--
-- TOC entry 199 (class 1259 OID 27621)
-- Name: ingresos_detalleclientereferencia; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_detalleclientereferencia (
    id integer NOT NULL,
    cliente_id integer NOT NULL,
    referencia_id integer NOT NULL,
    "medidorDeReferencia" character varying(10) NOT NULL,
    ubicacion_id integer NOT NULL
);


ALTER TABLE public.ingresos_detalleclientereferencia OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 27624)
-- Name: ingresos_detalleclientereferencia_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ingresos_detalleclientereferencia_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ingresos_detalleclientereferencia_id_seq OWNER TO postgres;

--
-- TOC entry 2652 (class 0 OID 0)
-- Dependencies: 200
-- Name: ingresos_detalleclientereferencia_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE ingresos_detalleclientereferencia_id_seq OWNED BY ingresos_detalleclientereferencia.id;


--
-- TOC entry 201 (class 1259 OID 27626)
-- Name: ingresos_detalledeactividad; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_detalledeactividad (
    id integer NOT NULL,
    rubro_id integer NOT NULL,
    actividad_id integer NOT NULL
);


ALTER TABLE public.ingresos_detalledeactividad OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 27629)
-- Name: ingresos_detalledeactividad_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ingresos_detalledeactividad_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ingresos_detalledeactividad_id_seq OWNER TO postgres;

--
-- TOC entry 2653 (class 0 OID 0)
-- Dependencies: 202
-- Name: ingresos_detalledeactividad_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE ingresos_detalledeactividad_id_seq OWNED BY ingresos_detalledeactividad.id;


--
-- TOC entry 203 (class 1259 OID 27631)
-- Name: ingresos_empleado; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_empleado (
    id integer NOT NULL,
    nombre character varying(20) NOT NULL,
    apellido character varying(20) NOT NULL,
    telefono character varying(10) NOT NULL,
    correo character varying(20) NOT NULL,
    observacion character varying(50) NOT NULL
);


ALTER TABLE public.ingresos_empleado OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 27634)
-- Name: ingresos_empleado_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ingresos_empleado_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ingresos_empleado_id_seq OWNER TO postgres;

--
-- TOC entry 2654 (class 0 OID 0)
-- Dependencies: 204
-- Name: ingresos_empleado_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE ingresos_empleado_id_seq OWNED BY ingresos_empleado.id;


--
-- TOC entry 205 (class 1259 OID 27636)
-- Name: ingresos_estadodeunainstalacion; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_estadodeunainstalacion (
    id smallint NOT NULL,
    descripcion character varying(25) NOT NULL,
    CONSTRAINT ingresos_estadodeunainstalacion_id_check CHECK ((id >= 0))
);


ALTER TABLE public.ingresos_estadodeunainstalacion OWNER TO postgres;

--
-- TOC entry 206 (class 1259 OID 27640)
-- Name: ingresos_formadeconexion; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_formadeconexion (
    id smallint NOT NULL,
    descripcion character varying(50) NOT NULL,
    CONSTRAINT ingresos_formadeconexion_id_check CHECK ((id >= 0))
);


ALTER TABLE public.ingresos_formadeconexion OWNER TO postgres;

--
-- TOC entry 207 (class 1259 OID 27644)
-- Name: ingresos_foto; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_foto (
    id integer NOT NULL,
    actividad_id integer,
    observacion character varying(50),
    ruta character varying(255)
);


ALTER TABLE public.ingresos_foto OWNER TO postgres;

--
-- TOC entry 208 (class 1259 OID 27647)
-- Name: ingresos_foto_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ingresos_foto_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ingresos_foto_id_seq OWNER TO postgres;

--
-- TOC entry 2655 (class 0 OID 0)
-- Dependencies: 208
-- Name: ingresos_foto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE ingresos_foto_id_seq OWNED BY ingresos_foto.id;


--
-- TOC entry 209 (class 1259 OID 27649)
-- Name: ingresos_instalador; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_instalador (
    id integer NOT NULL,
    nombre_id integer NOT NULL,
    cuadrilla_id integer,
    observacion character varying(50) NOT NULL
);


ALTER TABLE public.ingresos_instalador OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 27652)
-- Name: ingresos_instalador_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ingresos_instalador_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ingresos_instalador_id_seq OWNER TO postgres;

--
-- TOC entry 2656 (class 0 OID 0)
-- Dependencies: 210
-- Name: ingresos_instalador_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE ingresos_instalador_id_seq OWNED BY ingresos_instalador.id;


--
-- TOC entry 211 (class 1259 OID 27654)
-- Name: ingresos_materialdeactividad; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_materialdeactividad (
    id integer NOT NULL,
    material_id integer NOT NULL,
    actividad_id integer NOT NULL,
    cantidad numeric(4,2) NOT NULL,
    observacion character varying(50)
);


ALTER TABLE public.ingresos_materialdeactividad OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 27657)
-- Name: ingresos_materialdeactividad_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ingresos_materialdeactividad_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ingresos_materialdeactividad_id_seq OWNER TO postgres;

--
-- TOC entry 2657 (class 0 OID 0)
-- Dependencies: 212
-- Name: ingresos_materialdeactividad_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE ingresos_materialdeactividad_id_seq OWNED BY ingresos_materialdeactividad.id;


--
-- TOC entry 213 (class 1259 OID 27659)
-- Name: ingresos_modelodemedidor; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_modelodemedidor (
    id character varying(7) NOT NULL,
    descripcion character varying(50) NOT NULL
);


ALTER TABLE public.ingresos_modelodemedidor OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 27662)
-- Name: ingresos_motivoparasolicitud; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_motivoparasolicitud (
    id smallint NOT NULL,
    descripcion character varying(25) NOT NULL,
    CONSTRAINT ingresos_motivoparasolicitud_id_check CHECK ((id >= 0))
);


ALTER TABLE public.ingresos_motivoparasolicitud OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 27666)
-- Name: ingresos_nivelsocieconomico; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_nivelsocieconomico (
    id character varying(2) NOT NULL,
    descripcion character varying(15) NOT NULL
);


ALTER TABLE public.ingresos_nivelsocieconomico OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 27669)
-- Name: ingresos_parroquia; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_parroquia (
    id integer NOT NULL,
    num smallint NOT NULL,
    descripcion character varying(40) NOT NULL,
    canton_id integer,
    CONSTRAINT ingresos_parroquia_num_check CHECK ((num >= 0))
);


ALTER TABLE public.ingresos_parroquia OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 27673)
-- Name: ingresos_parroquia_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ingresos_parroquia_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ingresos_parroquia_id_seq OWNER TO postgres;

--
-- TOC entry 2658 (class 0 OID 0)
-- Dependencies: 217
-- Name: ingresos_parroquia_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE ingresos_parroquia_id_seq OWNED BY ingresos_parroquia.id;


--
-- TOC entry 218 (class 1259 OID 27675)
-- Name: ingresos_provincia; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_provincia (
    id smallint NOT NULL,
    descripcion character varying(20),
    CONSTRAINT ingresos_provincia_id_check CHECK ((id >= 0))
);


ALTER TABLE public.ingresos_provincia OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 27679)
-- Name: ingresos_ruta; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_ruta (
    id integer NOT NULL,
    num smallint NOT NULL,
    descripcion character varying(30),
    sector_id integer NOT NULL,
    CONSTRAINT ingresos_ruta_num_check CHECK ((num >= 0))
);


ALTER TABLE public.ingresos_ruta OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 27683)
-- Name: ingresos_ruta_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ingresos_ruta_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ingresos_ruta_id_seq OWNER TO postgres;

--
-- TOC entry 2659 (class 0 OID 0)
-- Dependencies: 220
-- Name: ingresos_ruta_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE ingresos_ruta_id_seq OWNED BY ingresos_ruta.id;


--
-- TOC entry 221 (class 1259 OID 27685)
-- Name: ingresos_sector; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_sector (
    id integer NOT NULL,
    num smallint NOT NULL,
    descripcion character varying(40),
    canton_id integer NOT NULL,
    CONSTRAINT ingresos_sector_num_check CHECK ((num >= 0))
);


ALTER TABLE public.ingresos_sector OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 27689)
-- Name: ingresos_sector_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ingresos_sector_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ingresos_sector_id_seq OWNER TO postgres;

--
-- TOC entry 2660 (class 0 OID 0)
-- Dependencies: 222
-- Name: ingresos_sector_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE ingresos_sector_id_seq OWNED BY ingresos_sector.id;


--
-- TOC entry 223 (class 1259 OID 27691)
-- Name: ingresos_secuencia; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_secuencia (
    id integer NOT NULL,
    num smallint NOT NULL,
    descripcion character varying(30),
    ruta_id integer NOT NULL,
    CONSTRAINT ingresos_secuencia_num_check CHECK ((num >= 0))
);


ALTER TABLE public.ingresos_secuencia OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 27695)
-- Name: ingresos_secuencia_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ingresos_secuencia_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ingresos_secuencia_id_seq OWNER TO postgres;

--
-- TOC entry 2661 (class 0 OID 0)
-- Dependencies: 224
-- Name: ingresos_secuencia_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE ingresos_secuencia_id_seq OWNED BY ingresos_secuencia.id;


--
-- TOC entry 225 (class 1259 OID 27697)
-- Name: ingresos_tipocalle; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_tipocalle (
    descripcion character varying(50),
    id character varying(2) NOT NULL
);


ALTER TABLE public.ingresos_tipocalle OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 27700)
-- Name: ingresos_tipodeacometidared; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_tipodeacometidared (
    id character varying(2) NOT NULL,
    descripcion character varying(25) NOT NULL
);


ALTER TABLE public.ingresos_tipodeacometidared OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 27703)
-- Name: ingresos_tipodeconstruccion; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_tipodeconstruccion (
    id smallint NOT NULL,
    descripcion character varying(50) NOT NULL,
    CONSTRAINT ingresos_tipodeconstruccion_id_check CHECK ((id >= 0))
);


ALTER TABLE public.ingresos_tipodeconstruccion OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 27707)
-- Name: ingresos_tipodeservicio; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_tipodeservicio (
    id character varying(3) NOT NULL,
    tension character varying(15) NOT NULL,
    descripcion character varying(25) NOT NULL
);


ALTER TABLE public.ingresos_tipodeservicio OWNER TO postgres;

--
-- TOC entry 229 (class 1259 OID 27710)
-- Name: ingresos_tipodesolicitud; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_tipodesolicitud (
    id smallint NOT NULL,
    descripcion character varying(25) NOT NULL,
    CONSTRAINT ingresos_tipodesolicitud_id_check CHECK ((id >= 0))
);


ALTER TABLE public.ingresos_tipodesolicitud OWNER TO postgres;

--
-- TOC entry 230 (class 1259 OID 27714)
-- Name: ingresos_ubicacion; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_ubicacion (
    id integer NOT NULL,
    parroquia_id integer NOT NULL,
    calle_id integer,
    interseccion_id integer,
    urbanizacion_id integer,
    caserio_id integer
);


ALTER TABLE public.ingresos_ubicacion OWNER TO postgres;

--
-- TOC entry 231 (class 1259 OID 27717)
-- Name: ingresos_ubicacion_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ingresos_ubicacion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ingresos_ubicacion_id_seq OWNER TO postgres;

--
-- TOC entry 2662 (class 0 OID 0)
-- Dependencies: 231
-- Name: ingresos_ubicacion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE ingresos_ubicacion_id_seq OWNED BY ingresos_ubicacion.id;


--
-- TOC entry 232 (class 1259 OID 27719)
-- Name: ingresos_ubicaciondelmedidor; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_ubicaciondelmedidor (
    id smallint NOT NULL,
    descripcion character varying(25) NOT NULL,
    CONSTRAINT ingresos_ubicaciondelmedidor_id_check CHECK ((id >= 0))
);


ALTER TABLE public.ingresos_ubicaciondelmedidor OWNER TO postgres;

--
-- TOC entry 233 (class 1259 OID 27723)
-- Name: ingresos_urbanizacion; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_urbanizacion (
    id integer NOT NULL,
    descripcion character varying(50) NOT NULL
);


ALTER TABLE public.ingresos_urbanizacion OWNER TO postgres;

--
-- TOC entry 234 (class 1259 OID 27726)
-- Name: ingresos_urbanizacion_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ingresos_urbanizacion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ingresos_urbanizacion_id_seq OWNER TO postgres;

--
-- TOC entry 2663 (class 0 OID 0)
-- Dependencies: 234
-- Name: ingresos_urbanizacion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE ingresos_urbanizacion_id_seq OWNED BY ingresos_urbanizacion.id;


--
-- TOC entry 235 (class 1259 OID 27728)
-- Name: ingresos_usodeenergia; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_usodeenergia (
    id character varying(2) NOT NULL,
    descripcion character varying(50) NOT NULL
);


ALTER TABLE public.ingresos_usodeenergia OWNER TO postgres;

--
-- TOC entry 236 (class 1259 OID 27731)
-- Name: ingresos_usoespecificodelinmueble; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_usoespecificodelinmueble (
    id smallint NOT NULL,
    "usoGeneral_id" integer NOT NULL,
    descripcion character varying(50) NOT NULL,
    CONSTRAINT ingresos_usoespecificodelinmueble_id_check CHECK ((id >= 0))
);


ALTER TABLE public.ingresos_usoespecificodelinmueble OWNER TO postgres;

--
-- TOC entry 237 (class 1259 OID 27735)
-- Name: ingresos_usogeneraldelinmueble; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ingresos_usogeneraldelinmueble (
    id smallint NOT NULL,
    descripcion character varying(25) NOT NULL,
    CONSTRAINT ingresos_usogeneraldelinmueble_id_check CHECK ((id >= 0))
);


ALTER TABLE public.ingresos_usogeneraldelinmueble OWNER TO postgres;

--
-- TOC entry 238 (class 1259 OID 27739)
-- Name: inventario_contrato; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE inventario_contrato (
    num character varying(10) NOT NULL,
    descripcion character varying(150) NOT NULL,
    zonas character varying(150) NOT NULL,
    "codigoInstalador" smallint NOT NULL,
    "inicioVigencia" date NOT NULL,
    "finalVigencia" date NOT NULL,
    CONSTRAINT "inventario_contrato_codigoInstalador_check" CHECK (("codigoInstalador" >= 0))
);


ALTER TABLE public.inventario_contrato OWNER TO postgres;

--
-- TOC entry 239 (class 1259 OID 27743)
-- Name: inventario_detallematerialcontrato; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE inventario_detallematerialcontrato (
    id integer NOT NULL,
    material_id integer NOT NULL,
    contrato_id character varying(10) NOT NULL,
    stock bigint NOT NULL,
    unidad character varying(15) NOT NULL,
    proporcionado boolean NOT NULL
);


ALTER TABLE public.inventario_detallematerialcontrato OWNER TO postgres;

--
-- TOC entry 240 (class 1259 OID 27746)
-- Name: inventario_detallematerialcontrato_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE inventario_detallematerialcontrato_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.inventario_detallematerialcontrato_id_seq OWNER TO postgres;

--
-- TOC entry 2664 (class 0 OID 0)
-- Dependencies: 240
-- Name: inventario_detallematerialcontrato_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE inventario_detallematerialcontrato_id_seq OWNED BY inventario_detallematerialcontrato.id;


--
-- TOC entry 241 (class 1259 OID 27748)
-- Name: inventario_detallerubro; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE inventario_detallerubro (
    id integer NOT NULL,
    contrato_id character varying(10) NOT NULL,
    servicio_id integer NOT NULL,
    rubro_id integer NOT NULL,
    "precioUnitario" numeric(10,2) NOT NULL
);


ALTER TABLE public.inventario_detallerubro OWNER TO postgres;

--
-- TOC entry 242 (class 1259 OID 27751)
-- Name: inventario_detallerubro_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE inventario_detallerubro_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.inventario_detallerubro_id_seq OWNER TO postgres;

--
-- TOC entry 2665 (class 0 OID 0)
-- Dependencies: 242
-- Name: inventario_detallerubro_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE inventario_detallerubro_id_seq OWNED BY inventario_detallerubro.id;


--
-- TOC entry 243 (class 1259 OID 27753)
-- Name: inventario_marca; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE inventario_marca (
    id character varying(3) NOT NULL,
    descripcion character varying(25) NOT NULL
);


ALTER TABLE public.inventario_marca OWNER TO postgres;

--
-- TOC entry 244 (class 1259 OID 27756)
-- Name: inventario_material; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE inventario_material (
    id integer NOT NULL,
    descripcion character varying(25) NOT NULL,
    "voltajeSoportado" smallint NOT NULL,
    CONSTRAINT "inventario_material_voltajeSoportado_check" CHECK (("voltajeSoportado" >= 0))
);


ALTER TABLE public.inventario_material OWNER TO postgres;

--
-- TOC entry 245 (class 1259 OID 27760)
-- Name: inventario_material_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE inventario_material_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.inventario_material_id_seq OWNER TO postgres;

--
-- TOC entry 2666 (class 0 OID 0)
-- Dependencies: 245
-- Name: inventario_material_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE inventario_material_id_seq OWNED BY inventario_material.id;


--
-- TOC entry 246 (class 1259 OID 27762)
-- Name: inventario_medidor; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE inventario_medidor (
    id integer NOT NULL,
    contrato_id integer,
    fabrica character varying(11) NOT NULL,
    serie character varying(9) NOT NULL,
    marca_id character varying(3) NOT NULL,
    tipo character varying(15) NOT NULL,
    digitos smallint NOT NULL,
    hilos smallint NOT NULL,
    fases smallint NOT NULL,
    voltaje smallint NOT NULL,
    est boolean NOT NULL,
    modelo_id character varying(6),
    CONSTRAINT inventario_medidor_digitos_check CHECK ((digitos >= 0)),
    CONSTRAINT inventario_medidor_fases_check CHECK ((fases >= 0)),
    CONSTRAINT inventario_medidor_hilos_check CHECK ((hilos >= 0)),
    CONSTRAINT inventario_medidor_voltaje_check CHECK ((voltaje >= 0))
);


ALTER TABLE public.inventario_medidor OWNER TO postgres;

--
-- TOC entry 247 (class 1259 OID 27769)
-- Name: inventario_medidor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE inventario_medidor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.inventario_medidor_id_seq OWNER TO postgres;

--
-- TOC entry 2667 (class 0 OID 0)
-- Dependencies: 247
-- Name: inventario_medidor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE inventario_medidor_id_seq OWNED BY inventario_medidor.id;


--
-- TOC entry 248 (class 1259 OID 27771)
-- Name: inventario_rangodematerial; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE inventario_rangodematerial (
    id integer NOT NULL,
    "detalleMaterialContrato_id" integer NOT NULL,
    inicio numeric(10,0) NOT NULL,
    final numeric(10,0) NOT NULL
);


ALTER TABLE public.inventario_rangodematerial OWNER TO postgres;

--
-- TOC entry 249 (class 1259 OID 27774)
-- Name: inventario_rangodematerial_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE inventario_rangodematerial_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.inventario_rangodematerial_id_seq OWNER TO postgres;

--
-- TOC entry 2668 (class 0 OID 0)
-- Dependencies: 249
-- Name: inventario_rangodematerial_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE inventario_rangodematerial_id_seq OWNED BY inventario_rangodematerial.id;


--
-- TOC entry 250 (class 1259 OID 27776)
-- Name: inventario_rubro; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE inventario_rubro (
    id integer NOT NULL,
    descripcion character varying(25) NOT NULL
);


ALTER TABLE public.inventario_rubro OWNER TO postgres;

--
-- TOC entry 251 (class 1259 OID 27779)
-- Name: inventario_rubro_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE inventario_rubro_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.inventario_rubro_id_seq OWNER TO postgres;

--
-- TOC entry 2669 (class 0 OID 0)
-- Dependencies: 251
-- Name: inventario_rubro_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE inventario_rubro_id_seq OWNED BY inventario_rubro.id;


--
-- TOC entry 252 (class 1259 OID 27781)
-- Name: inventario_sello; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE inventario_sello (
    id integer NOT NULL,
    "detalleMaterialContrato_id" integer NOT NULL,
    numero character varying(10) NOT NULL,
    color character varying(20) NOT NULL,
    ubicacion character varying(10) NOT NULL,
    estado smallint NOT NULL,
    CONSTRAINT inventario_sello_estado_check CHECK ((estado >= 0))
);


ALTER TABLE public.inventario_sello OWNER TO postgres;

--
-- TOC entry 253 (class 1259 OID 27785)
-- Name: inventario_sello_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE inventario_sello_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.inventario_sello_id_seq OWNER TO postgres;

--
-- TOC entry 2670 (class 0 OID 0)
-- Dependencies: 253
-- Name: inventario_sello_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE inventario_sello_id_seq OWNED BY inventario_sello.id;


--
-- TOC entry 254 (class 1259 OID 27787)
-- Name: inventario_servicio; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE inventario_servicio (
    id integer NOT NULL,
    descripcion character varying(25) NOT NULL
);


ALTER TABLE public.inventario_servicio OWNER TO postgres;

--
-- TOC entry 255 (class 1259 OID 27790)
-- Name: inventario_servicio_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE inventario_servicio_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.inventario_servicio_id_seq OWNER TO postgres;

--
-- TOC entry 2671 (class 0 OID 0)
-- Dependencies: 255
-- Name: inventario_servicio_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE inventario_servicio_id_seq OWNED BY inventario_servicio.id;


--
-- TOC entry 256 (class 1259 OID 27792)
-- Name: inventario_subtipodematerial; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE inventario_subtipodematerial (
    id integer NOT NULL,
    "tipoDeMaterial_id" integer NOT NULL,
    descripcion character varying(25) NOT NULL
);


ALTER TABLE public.inventario_subtipodematerial OWNER TO postgres;

--
-- TOC entry 257 (class 1259 OID 27795)
-- Name: inventario_subtipodematerial_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE inventario_subtipodematerial_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.inventario_subtipodematerial_id_seq OWNER TO postgres;

--
-- TOC entry 2672 (class 0 OID 0)
-- Dependencies: 257
-- Name: inventario_subtipodematerial_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE inventario_subtipodematerial_id_seq OWNED BY inventario_subtipodematerial.id;


--
-- TOC entry 258 (class 1259 OID 27797)
-- Name: inventario_tipodematerial; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE inventario_tipodematerial (
    id integer NOT NULL,
    material_id integer NOT NULL,
    descripcion character varying(25) NOT NULL
);


ALTER TABLE public.inventario_tipodematerial OWNER TO postgres;

--
-- TOC entry 259 (class 1259 OID 27800)
-- Name: inventario_tipodematerial_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE inventario_tipodematerial_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.inventario_tipodematerial_id_seq OWNER TO postgres;

--
-- TOC entry 2673 (class 0 OID 0)
-- Dependencies: 259
-- Name: inventario_tipodematerial_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE inventario_tipodematerial_id_seq OWNED BY inventario_tipodematerial.id;


--
-- TOC entry 260 (class 1259 OID 27802)
-- Name: usuarios_usuariosico; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE usuarios_usuariosico (
    id integer NOT NULL,
    nombre character varying(10) NOT NULL,
    clave character varying(10) NOT NULL,
    contrato_id character varying(10) NOT NULL
);


ALTER TABLE public.usuarios_usuariosico OWNER TO postgres;

--
-- TOC entry 261 (class 1259 OID 27805)
-- Name: usuarios_usuariosico_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE usuarios_usuariosico_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.usuarios_usuariosico_id_seq OWNER TO postgres;

--
-- TOC entry 2674 (class 0 OID 0)
-- Dependencies: 261
-- Name: usuarios_usuariosico_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE usuarios_usuariosico_id_seq OWNED BY usuarios_usuariosico.id;


--
-- TOC entry 2067 (class 2604 OID 27807)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- TOC entry 2068 (class 2604 OID 27808)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- TOC entry 2069 (class 2604 OID 27809)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- TOC entry 2070 (class 2604 OID 27810)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- TOC entry 2071 (class 2604 OID 27811)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- TOC entry 2072 (class 2604 OID 27812)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- TOC entry 2073 (class 2604 OID 27813)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_usuario_sico ALTER COLUMN id SET DEFAULT nextval('auth_user_usuario_sico_id_seq'::regclass);


--
-- TOC entry 2074 (class 2604 OID 27814)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY busquedas_vitacorabusquedas ALTER COLUMN id SET DEFAULT nextval('busquedas_vitacorabusquedas_id_seq'::regclass);


--
-- TOC entry 2075 (class 2604 OID 27815)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- TOC entry 2077 (class 2604 OID 27816)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- TOC entry 2078 (class 2604 OID 27817)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_actividad ALTER COLUMN id SET DEFAULT nextval('ingresos_actividad_id_seq'::regclass);


--
-- TOC entry 2080 (class 2604 OID 27818)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_calle ALTER COLUMN id SET DEFAULT nextval('ingresos_calle_id_seq'::regclass);


--
-- TOC entry 2081 (class 2604 OID 27819)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_canton ALTER COLUMN id SET DEFAULT nextval('ingresos_canton_id_seq'::regclass);


--
-- TOC entry 2083 (class 2604 OID 27820)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_caserio ALTER COLUMN id SET DEFAULT nextval('ingresos_caserio_id_seq'::regclass);


--
-- TOC entry 2084 (class 2604 OID 27821)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_cliente ALTER COLUMN id SET DEFAULT nextval('ingresos_cliente_id_seq'::regclass);


--
-- TOC entry 2086 (class 2604 OID 27822)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_cuadrilla ALTER COLUMN id SET DEFAULT nextval('ingresos_cuadrilla_id_seq'::regclass);


--
-- TOC entry 2088 (class 2604 OID 27823)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_detalleclientemedidor ALTER COLUMN id SET DEFAULT nextval('ingresos_detalleclientemedidor_id_seq'::regclass);


--
-- TOC entry 2089 (class 2604 OID 27824)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_detalleclientereferencia ALTER COLUMN id SET DEFAULT nextval('ingresos_detalleclientereferencia_id_seq'::regclass);


--
-- TOC entry 2090 (class 2604 OID 27825)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_detalledeactividad ALTER COLUMN id SET DEFAULT nextval('ingresos_detalledeactividad_id_seq'::regclass);


--
-- TOC entry 2091 (class 2604 OID 27826)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_empleado ALTER COLUMN id SET DEFAULT nextval('ingresos_empleado_id_seq'::regclass);


--
-- TOC entry 2094 (class 2604 OID 27827)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_foto ALTER COLUMN id SET DEFAULT nextval('ingresos_foto_id_seq'::regclass);


--
-- TOC entry 2095 (class 2604 OID 27828)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_instalador ALTER COLUMN id SET DEFAULT nextval('ingresos_instalador_id_seq'::regclass);


--
-- TOC entry 2096 (class 2604 OID 27829)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_materialdeactividad ALTER COLUMN id SET DEFAULT nextval('ingresos_materialdeactividad_id_seq'::regclass);


--
-- TOC entry 2098 (class 2604 OID 27830)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_parroquia ALTER COLUMN id SET DEFAULT nextval('ingresos_parroquia_id_seq'::regclass);


--
-- TOC entry 2101 (class 2604 OID 27831)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_ruta ALTER COLUMN id SET DEFAULT nextval('ingresos_ruta_id_seq'::regclass);


--
-- TOC entry 2103 (class 2604 OID 27832)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_sector ALTER COLUMN id SET DEFAULT nextval('ingresos_sector_id_seq'::regclass);


--
-- TOC entry 2105 (class 2604 OID 27833)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_secuencia ALTER COLUMN id SET DEFAULT nextval('ingresos_secuencia_id_seq'::regclass);


--
-- TOC entry 2109 (class 2604 OID 27834)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_ubicacion ALTER COLUMN id SET DEFAULT nextval('ingresos_ubicacion_id_seq'::regclass);


--
-- TOC entry 2111 (class 2604 OID 27835)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_urbanizacion ALTER COLUMN id SET DEFAULT nextval('ingresos_urbanizacion_id_seq'::regclass);


--
-- TOC entry 2115 (class 2604 OID 27836)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_detallematerialcontrato ALTER COLUMN id SET DEFAULT nextval('inventario_detallematerialcontrato_id_seq'::regclass);


--
-- TOC entry 2116 (class 2604 OID 27837)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_detallerubro ALTER COLUMN id SET DEFAULT nextval('inventario_detallerubro_id_seq'::regclass);


--
-- TOC entry 2117 (class 2604 OID 27838)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_material ALTER COLUMN id SET DEFAULT nextval('inventario_material_id_seq'::regclass);


--
-- TOC entry 2119 (class 2604 OID 27839)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_medidor ALTER COLUMN id SET DEFAULT nextval('inventario_medidor_id_seq'::regclass);


--
-- TOC entry 2124 (class 2604 OID 27840)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_rangodematerial ALTER COLUMN id SET DEFAULT nextval('inventario_rangodematerial_id_seq'::regclass);


--
-- TOC entry 2125 (class 2604 OID 27841)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_rubro ALTER COLUMN id SET DEFAULT nextval('inventario_rubro_id_seq'::regclass);


--
-- TOC entry 2126 (class 2604 OID 27842)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_sello ALTER COLUMN id SET DEFAULT nextval('inventario_sello_id_seq'::regclass);


--
-- TOC entry 2128 (class 2604 OID 27843)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_servicio ALTER COLUMN id SET DEFAULT nextval('inventario_servicio_id_seq'::regclass);


--
-- TOC entry 2129 (class 2604 OID 27844)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_subtipodematerial ALTER COLUMN id SET DEFAULT nextval('inventario_subtipodematerial_id_seq'::regclass);


--
-- TOC entry 2130 (class 2604 OID 27845)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_tipodematerial ALTER COLUMN id SET DEFAULT nextval('inventario_tipodematerial_id_seq'::regclass);


--
-- TOC entry 2131 (class 2604 OID 27846)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY usuarios_usuariosico ALTER COLUMN id SET DEFAULT nextval('usuarios_usuariosico_id_seq'::regclass);


--
-- TOC entry 2526 (class 0 OID 27513)
-- Dependencies: 161
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- TOC entry 2675 (class 0 OID 0)
-- Dependencies: 162
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- TOC entry 2528 (class 0 OID 27518)
-- Dependencies: 163
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- TOC entry 2676 (class 0 OID 0)
-- Dependencies: 164
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- TOC entry 2530 (class 0 OID 27523)
-- Dependencies: 165
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add permission	1	add_permission
2	Can change permission	1	change_permission
3	Can delete permission	1	delete_permission
4	Can add group	2	add_group
5	Can change group	2	change_group
6	Can delete group	2	delete_group
7	Can add user	3	add_user
8	Can change user	3	change_user
9	Can delete user	3	delete_user
10	Can add content type	4	add_contenttype
11	Can change content type	4	change_contenttype
12	Can delete content type	4	delete_contenttype
13	Can add session	5	add_session
14	Can change session	5	change_session
15	Can delete session	5	delete_session
16	Can add log entry	6	add_logentry
17	Can change log entry	6	change_logentry
18	Can delete log entry	6	delete_logentry
19	Can add Registro de Búsqueda	7	add_vitacorabusquedas
20	Can change Registro de Búsqueda	7	change_vitacorabusquedas
21	Can delete Registro de Búsqueda	7	delete_vitacorabusquedas
22	Can add provincia	8	add_provincia
23	Can change provincia	8	change_provincia
24	Can delete provincia	8	delete_provincia
25	Can add canton	9	add_canton
26	Can change canton	9	change_canton
27	Can delete canton	9	delete_canton
28	Can add parroquia	10	add_parroquia
29	Can change parroquia	10	change_parroquia
30	Can delete parroquia	10	delete_parroquia
31	Can add sector	11	add_sector
32	Can change sector	11	change_sector
33	Can delete sector	11	delete_sector
34	Can add ruta	12	add_ruta
35	Can change ruta	12	change_ruta
36	Can delete ruta	12	delete_ruta
37	Can add Geocódigo	13	add_secuencia
38	Can change Geocódigo	13	change_secuencia
39	Can delete Geocódigo	13	delete_secuencia
40	Can add cliente	14	add_cliente
41	Can change cliente	14	change_cliente
42	Can delete cliente	14	delete_cliente
43	Can add Detalle Cliente-Medidor	15	add_detalleclientemedidor
44	Can change Detalle Cliente-Medidor	15	change_detalleclientemedidor
45	Can delete Detalle Cliente-Medidor	15	delete_detalleclientemedidor
46	Can add detalle cliente referencia	16	add_detalleclientereferencia
47	Can change detalle cliente referencia	16	change_detalleclientereferencia
48	Can delete detalle cliente referencia	16	delete_detalleclientereferencia
49	Can add Ubicación	17	add_ubicacion
50	Can change Ubicación	17	change_ubicacion
51	Can delete Ubicación	17	delete_ubicacion
52	Can add caserio	18	add_caserio
53	Can change caserio	18	change_caserio
54	Can delete caserio	18	delete_caserio
55	Can add Urbanización	19	add_urbanizacion
56	Can change Urbanización	19	change_urbanizacion
57	Can delete Urbanización	19	delete_urbanizacion
58	Can add calle	20	add_calle
59	Can change calle	20	change_calle
60	Can delete calle	20	delete_calle
61	Can add tipo calle	21	add_tipocalle
62	Can change tipo calle	21	change_tipocalle
63	Can delete tipo calle	21	delete_tipocalle
64	Can add Actividad	22	add_actividad
65	Can change Actividad	22	change_actividad
66	Can delete Actividad	22	delete_actividad
67	Can add Tipo de Construcción	23	add_tipodeconstruccion
68	Can change Tipo de Construcción	23	change_tipodeconstruccion
69	Can delete Tipo de Construcción	23	delete_tipodeconstruccion
70	Can add Clase de Red	24	add_clasered
71	Can change Clase de Red	24	change_clasered
72	Can delete Clase de Red	24	delete_clasered
73	Can add Calibre de Red	25	add_calibredelared
74	Can change Calibre de Red	25	change_calibredelared
75	Can delete Calibre de Red	25	delete_calibredelared
76	Can add Estado de una Instalación	26	add_estadodeunainstalacion
77	Can change Estado de una Instalación	26	change_estadodeunainstalacion
78	Can delete Estado de una Instalación	26	delete_estadodeunainstalacion
79	Can add Tipo de Acometida o Red	27	add_tipodeacometidared
80	Can change Tipo de Acometida o Red	27	change_tipodeacometidared
81	Can delete Tipo de Acometida o Red	27	delete_tipodeacometidared
82	Can add Uso de Energía	28	add_usodeenergia
83	Can change Uso de Energía	28	change_usodeenergia
84	Can delete Uso de Energía	28	delete_usodeenergia
85	Can add Uso General del Inmueble	29	add_usogeneraldelinmueble
86	Can change Uso General del Inmueble	29	change_usogeneraldelinmueble
87	Can delete Uso General del Inmueble	29	delete_usogeneraldelinmueble
88	Can add Uso Específico del Inmueble	30	add_usoespecificodelinmueble
89	Can change Uso Específico del Inmueble	30	change_usoespecificodelinmueble
90	Can delete Uso Específico del Inmueble	30	delete_usoespecificodelinmueble
91	Can add Modelo de Medidor	31	add_modelodemedidor
92	Can change Modelo de Medidor	31	change_modelodemedidor
93	Can delete Modelo de Medidor	31	delete_modelodemedidor
94	Can add Forma de Conexión	32	add_formadeconexion
95	Can change Forma de Conexión	32	change_formadeconexion
96	Can delete Forma de Conexión	32	delete_formadeconexion
97	Can add demanda	33	add_demanda
98	Can change demanda	33	change_demanda
99	Can delete demanda	33	delete_demanda
100	Can add Motivo para Solicitud	34	add_motivoparasolicitud
101	Can change Motivo para Solicitud	34	change_motivoparasolicitud
102	Can delete Motivo para Solicitud	34	delete_motivoparasolicitud
103	Can add Tipo de Solicitud	35	add_tipodesolicitud
104	Can change Tipo de Solicitud	35	change_tipodesolicitud
105	Can delete Tipo de Solicitud	35	delete_tipodesolicitud
106	Can add Tipo de Servicio	36	add_tipodeservicio
107	Can change Tipo de Servicio	36	change_tipodeservicio
108	Can delete Tipo de Servicio	36	delete_tipodeservicio
109	Can add Ubicación del Medidor	37	add_ubicaciondelmedidor
110	Can change Ubicación del Medidor	37	change_ubicaciondelmedidor
111	Can delete Ubicación del Medidor	37	delete_ubicaciondelmedidor
112	Can add cuadrilla	38	add_cuadrilla
113	Can change cuadrilla	38	change_cuadrilla
114	Can delete cuadrilla	38	delete_cuadrilla
115	Can add empleado	39	add_empleado
116	Can change empleado	39	change_empleado
117	Can delete empleado	39	delete_empleado
118	Can add instalador	40	add_instalador
119	Can change instalador	40	change_instalador
120	Can delete instalador	40	delete_instalador
121	Can add material de actividad	41	add_materialdeactividad
122	Can change material de actividad	41	change_materialdeactividad
123	Can delete material de actividad	41	delete_materialdeactividad
124	Can add Rubro de Actividad	42	add_detalledeactividad
125	Can change Rubro de Actividad	42	change_detalledeactividad
126	Can delete Rubro de Actividad	42	delete_detalledeactividad
127	Can add Foto	43	add_foto
128	Can change Foto	43	change_foto
129	Can delete Foto	43	delete_foto
130	Can add Nivel Socioeconómico	44	add_nivelsocieconomico
131	Can change Nivel Socioeconómico	44	change_nivelsocieconomico
132	Can delete Nivel Socioeconómico	44	delete_nivelsocieconomico
133	Can add contrato	45	add_contrato
134	Can change contrato	45	change_contrato
135	Can delete contrato	45	delete_contrato
136	Can add marca	46	add_marca
137	Can change marca	46	change_marca
138	Can delete marca	46	delete_marca
139	Can add medidor	47	add_medidor
140	Can change medidor	47	change_medidor
141	Can delete medidor	47	delete_medidor
142	Can add sello	48	add_sello
143	Can change sello	48	change_sello
144	Can delete sello	48	delete_sello
145	Can add subtipo de material	49	add_subtipodematerial
146	Can change subtipo de material	49	change_subtipodematerial
147	Can delete subtipo de material	49	delete_subtipodematerial
148	Can add tipo de material	50	add_tipodematerial
149	Can change tipo de material	50	change_tipodematerial
150	Can delete tipo de material	50	delete_tipodematerial
151	Can add material	51	add_material
152	Can change material	51	change_material
153	Can delete material	51	delete_material
154	Can add rango de material	52	add_rangodematerial
155	Can change rango de material	52	change_rangodematerial
156	Can delete rango de material	52	delete_rangodematerial
157	Can add detalle material contrato	53	add_detallematerialcontrato
158	Can change detalle material contrato	53	change_detallematerialcontrato
159	Can delete detalle material contrato	53	delete_detallematerialcontrato
160	Can add servicio	54	add_servicio
161	Can change servicio	54	change_servicio
162	Can delete servicio	54	delete_servicio
163	Can add rubro	55	add_rubro
164	Can change rubro	55	change_rubro
165	Can delete rubro	55	delete_rubro
166	Can add detalle rubro	56	add_detallerubro
167	Can change detalle rubro	56	change_detallerubro
168	Can delete detalle rubro	56	delete_detallerubro
169	Can add Usuario en Sico	57	add_usuariosico
170	Can change Usuario en Sico	57	change_usuariosico
171	Can delete Usuario en Sico	57	delete_usuariosico
\.


--
-- TOC entry 2677 (class 0 OID 0)
-- Dependencies: 166
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_permission_id_seq', 171, true);


--
-- TOC entry 2532 (class 0 OID 27528)
-- Dependencies: 167
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, sesion_sico) FROM stdin;
1	pbkdf2_sha256$12000$wNznJ4vpupKC$z8QW+30HSgVDX7/snI486d+Nvhkh7sJuT1g6jCuc5NM=	2014-11-24 16:22:20.934-05	t	jhonsson	Jhonsson	Córdova	admin@admin.com	t	t	2014-11-23 05:25:22-05	
\.


--
-- TOC entry 2533 (class 0 OID 27531)
-- Dependencies: 168
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- TOC entry 2678 (class 0 OID 0)
-- Dependencies: 169
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- TOC entry 2679 (class 0 OID 0)
-- Dependencies: 170
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_id_seq', 1, true);


--
-- TOC entry 2536 (class 0 OID 27538)
-- Dependencies: 171
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- TOC entry 2680 (class 0 OID 0)
-- Dependencies: 172
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- TOC entry 2538 (class 0 OID 27543)
-- Dependencies: 173
-- Data for Name: auth_user_usuario_sico; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_usuario_sico (id, user_id, usuariosico_id) FROM stdin;
1	1	1
\.


--
-- TOC entry 2681 (class 0 OID 0)
-- Dependencies: 174
-- Name: auth_user_usuario_sico_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_usuario_sico_id_seq', 1, true);


--
-- TOC entry 2540 (class 0 OID 27548)
-- Dependencies: 175
-- Data for Name: busquedas_vitacorabusquedas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY busquedas_vitacorabusquedas (id, "tipoBusq", "fechaHora", consulta, usuario_id, "estadoRetorno") FROM stdin;
\.


--
-- TOC entry 2682 (class 0 OID 0)
-- Dependencies: 176
-- Name: busquedas_vitacorabusquedas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('busquedas_vitacorabusquedas_id_seq', 1, false);


--
-- TOC entry 2542 (class 0 OID 27553)
-- Dependencies: 177
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_admin_log (id, action_time, user_id, content_type_id, object_id, object_repr, action_flag, change_message) FROM stdin;
1	2014-11-23 05:53:05.282-05	1	45	0000008-14	0000008-14	1	
2	2014-11-23 05:53:07.009-05	1	57	1	lzambrano - 0000008-14	1	
3	2014-11-23 05:53:10.033-05	1	3	1	jhonsson	2	Modificado/a first_name, last_name y usuario_sico.
4	2014-11-23 22:53:06.559-05	1	35	1	SERVICIO NUEVO	1	
5	2014-11-23 22:53:10.296-05	1	35	1	SERVICIO NUEVO	2	No ha cambiado ningún campo.
6	2014-11-23 22:53:27.955-05	1	35	11	CAMBIO DE MATERIALES	1	
7	2014-11-23 22:53:42.017-05	1	35	13	CAMBIO DE MEDIDOR	1	
8	2014-11-23 22:54:14.344-05	1	26	1	ACEPTABLE	1	
9	2014-11-23 22:54:23.457-05	1	26	2	DEFICIENTE	1	
10	2014-11-23 22:54:32.577-05	1	26	3	REGULAR	1	
11	2014-11-23 22:54:55.803-05	1	26	4	SIN INSTALACION E.C.	1	
12	2014-11-23 22:55:25.028-05	1	28	RD	RESIDENCIAL	1	
13	2014-11-23 23:12:52.96-05	1	28	AS	ASISTENCIA SOCIAL BAJA TENSION	1	
14	2014-11-23 23:13:29.113-05	1	28	AB	ASISTENCIA SOCIAL BT CON DEMANDA	1	
15	2014-11-23 23:13:53.411-05	1	28	A3	ASISTENCIA SOCIAL BT CON DEMANDA HORARIA	1	
16	2014-11-23 23:14:14.548-05	1	28	AD	ASISTENCIA SOCIAL MEDIA TENSION	1	
17	2014-11-23 23:15:08.309-05	1	28	AH	ASISTENCIA SOCIAL MT CON DEMANDA HORARIA	1	
18	2014-11-23 23:15:51.773-05	1	28	T3	ASISTENCIA SOCIAL TERCERA EDAD BT DEMANDA HORARIA	1	
19	2014-11-23 23:16:21.816-05	1	28	AU	AUTOCONSUMO BAJA TERNSION	1	
20	2014-11-23 23:16:59.186-05	1	28	GD	AUTOCONSUMO CON DEMANDA HORARIA	1	
21	2014-11-23 23:17:27.074-05	1	28	DH	AUTOCONSUMO DEMANDA HORARIA	1	
22	2014-11-23 23:18:12.057-05	1	28	DD	AUTOCONSUMO MT CON DEMANDA	1	
23	2014-11-23 23:21:45.644-05	1	28	AM	AUTOCONSUMO PARA LOCALES EMPRESA MT	1	
24	2014-11-23 23:22:10.569-05	1	28	BP	BENEFICIO PUBLICO BAJA TENSION	1	
25	2014-11-23 23:22:41.251-05	1	28	BB	BENEFICIO PUBLICO BT CON DEMANDA	1	
26	2014-11-23 23:23:11.396-05	1	28	B3	BENEFICIO PUBLICO BT CON DEMANDA HORARIA	1	
27	2014-11-23 23:27:38.926-05	1	28	BH	BENEFICIO PUBLICO CON DEMANDA HORARIA	1	
28	2014-11-23 23:28:09.127-05	1	28	BD	BENEFICIO PUBLICO MEDIA TENSION	1	
29	2014-11-23 23:28:54.015-05	1	28	BJ	BOMBEO AGUA JUNTAS ADMINISTRADORAS AGUA POTABLE	1	
30	2014-11-23 23:29:09.117-05	1	28	BA	BOMBEO DE AGUA	1	
31	2014-11-23 23:29:45.813-05	1	28	WA	BOMBEO DE AGUA AGRICOLA Y PSICOLA CON DEMANDA	1	
32	2014-11-23 23:30:12.614-05	1	28	FH	BOMBEO DE AGUA AGRICOLA Y PSICOLA HORARIO	1	
33	2014-11-23 23:33:04.812-05	1	28	W3	BOMBEO DE AGUA BT CON DEMANDA HORARIA	1	
34	2014-11-23 23:33:31.371-05	1	28	WD	BOMBEO DE AGUA CON DEMANDA	1	
35	2014-11-23 23:33:46.845-05	1	28	WH	BOMBEO DE AGUA CON DEMANDA HORARIA	1	
36	2014-11-23 23:34:38.033-05	1	28	DA	CAPACIDADES ESPECIALES - ENTIDADES AS. SOCIAL B.T.	1	
37	2014-11-23 23:35:05.102-05	1	28	DB	CAPACIDADES ESPECIALES - ENTIDADES DMA B.T.	1	
38	2014-11-23 23:35:29.927-05	1	28	DR	CAPACIDADES ESPECIALES - ENTIDADES HORARIOS	1	
39	2014-11-23 23:36:25.692-05	1	28	DN	CAPACIDAES ESPECIALES M.T. CON DEMANDA	1	
40	2014-11-23 23:36:52.608-05	1	28	XH	CLIENTES SERVIDOS EN ALTA TENSION	1	
41	2014-11-23 23:37:06.427-05	1	28	CO	COMERCIAL BAJA TENSION	1	
42	2014-11-23 23:37:19.196-05	1	28	CB	COMERCIAL BAJA TENSION CON DEMANDA	1	
43	2014-11-23 23:38:49.134-05	1	28	C3	COMERCIAL BT CON DEMANDA HORARIA	1	
44	2014-11-23 23:39:07.216-05	1	28	CH	COMERCIAL CON DEMANDA HORARIA	1	
45	2014-11-23 23:40:20.969-05	1	28	CD	COMERCIAL MEDIA TENSION	1	
46	2014-11-23 23:40:39.301-05	1	28	CR	CULTO RELIGIOSO BAJA TENSION	1	
47	2014-11-23 23:41:01.895-05	1	28	U3	CULTO RELIGIOSO BT CON DEMANDA	1	
48	2014-11-23 23:41:25.384-05	1	28	UH	CULTO RELIGIOSO CON DEMANDA HORARIA	1	
49	2014-11-23 23:45:17.839-05	1	28	CK	CULTO RELIGIOSO MEDIA TENSION	1	
50	2014-11-23 23:45:58.676-05	1	28	MB	ENTIDAD MUNICIPAL BT CON DEMANDA	1	
51	2014-11-23 23:46:36.795-05	1	28	OB	ENTIDAD OFICIAL BT CON DEMANDA	1	
52	2014-11-23 23:46:59.752-05	1	28	MU	ENTIDADES MUNICIPALES BAJA TENSION	1	
53	2014-11-23 23:47:49.188-05	1	28	M3	ENTIDADES MUNICIPALES BT CON DEMANDA HORARIA	1	
54	2014-11-23 23:48:16.54-05	1	28	MH	ENTIDADES MUNICIPALES CON DEMANDA HORARIA	1	
55	2014-11-23 23:48:39.85-05	1	28	MD	ENTIDADES MUNICIPALES MEDIA TENSION	1	
56	2014-11-23 23:49:16.567-05	1	28	OF	ENTIDADES OFICIALES BAJA TENSION	1	
57	2014-11-23 23:49:56.554-05	1	28	O3	ENTIDADES OFICIALES BT CON DEMANDA HORARIA	1	
58	2014-11-23 23:50:30.801-05	1	28	OH	ENTIDADES OFICIALES CON DEMANDA HORARIA	1	
59	2014-11-23 23:51:10.748-05	1	28	OD	ENTIDADES OFICIALES MEDIA TENSION	1	
60	2014-11-23 23:51:29.81-05	1	28	ES	ESCENARIO DEPORTIVO BAJA TENSION	1	
61	2014-11-23 23:52:22.261-05	1	28	E3	ESCENARIO DEPORTIVO BT CON DEMANDA HORARIA	1	
62	2014-11-23 23:52:42.69-05	1	28	EH	ESCENARIO DEPORTIVO CON DEMANDA HORARIA	1	
63	2014-11-23 23:53:32.802-05	1	28	ED	ESCENARIO DEPORTIVO MEDIA TENSION	1	
64	2014-11-23 23:57:12.928-05	1	28	IP	ILUMINACION PUBLICA BAJO MEDICION	1	
65	2014-11-23 23:57:32.497-05	1	28	IA	INDUSTRIAL ARTESANAL	1	
66	2014-11-23 23:57:52.335-05	1	28	IB	INDUSTRIAL BAJA TENSION CON DEMANDA	1	
67	2014-11-23 23:58:33.521-05	1	28	I3	INDUSTRIAL BT CON MEDICION HORARIA	1	
68	2014-11-23 23:59:00.894-05	1	28	IH	INDUSTRIAL CON MEDICION HORARIA	1	
69	2014-11-24 00:00:01.955-05	1	28	KH	INDUSTRIAL CON MEDICION HORARIA CON INCENDIOS AT	1	
70	2014-11-24 00:00:15.573-05	1	28	JH	INDUSTRIAL CON MEDICION HORARIA CON INCENDIOS MT	1	
71	2014-11-24 00:00:27.815-05	1	28	ID	INDUSTRIAL MEDIA TENSION	1	
72	2014-11-24 00:00:43.666-05	1	28	LH	LOCAL DEPORTIVO CON DEMANDA HORARIA	1	
73	2014-11-24 00:01:24.98-05	1	28	SH	PREVIO IND CON MEDICION HORARIA CON INCENTIVOS AT	1	
74	2014-11-24 00:01:37.211-05	1	28	RC	RESIDENCIAL COMUNITARIO	1	
75	2014-11-24 00:01:56.907-05	1	28	RT	RESIDENCIAL O DOMESTICO TEMPORAL	1	
76	2014-11-24 00:02:29.476-05	1	28	DS	RESIDENCIAL-CAPACIDAD ESPECIAL B.T.	1	
77	2014-11-24 00:02:47.291-05	1	28	DM	RESIDENCIAL-CAPACIDAD ESPECIAL M.T.	1	
78	2014-11-24 00:03:03.953-05	1	28	SC	SERVICIO COMUNITARIO BAJA TENSION	1	
79	2014-11-24 00:03:22.304-05	1	28	SD	SERVICIO COMUNITARIO MEDIA TENSION	1	
80	2014-11-24 00:03:40.696-05	1	28	TB	TERCERA EDAD ENTIDADES BT DEMANDA	1	
81	2014-11-24 00:03:54.237-05	1	28	VR	VENTA PARA REVENTA	1	
82	2014-11-24 00:23:32.253-05	1	34	2	PLAN REP - PERDIDAS	1	
83	2014-11-24 00:24:17.021-05	1	34	1	SOLICITADO CLIENTE	1	
84	2014-11-24 00:26:23.638-05	1	34	20	SOLIC. CONTROL PERDI.	1	
85	2014-11-24 00:43:51.417-05	1	23	1	ADOBE	1	
86	2014-11-24 00:44:02.18-05	1	23	2	BAHARENQUE	1	
87	2014-11-24 00:44:08.902-05	1	23	3	BLOQUE	1	
88	2014-11-24 00:44:18.632-05	1	23	13	CAÑA	1	
89	2014-11-24 00:44:26.959-05	1	23	4	CONCRETO	1	
90	2014-11-24 00:46:33.649-05	1	23	6	KIOSKO DE MADERA	1	
91	2014-11-24 00:46:48.873-05	1	23	5	KIOSKO METALICO	1	
92	2014-11-24 00:46:58.98-05	1	23	7	LADRILLO	1	
93	2014-11-24 00:47:14.348-05	1	23	14	LOTE VACIO	1	
94	2014-11-24 00:47:20.204-05	1	23	9	MADERA	1	
95	2014-11-24 00:47:27.863-05	1	23	8	MIXTA	1	
96	2014-11-24 00:47:38.989-05	1	23	12	NAVE INDUSTRIAL	1	
97	2014-11-24 00:47:49.853-05	1	23	10	PANEL LUMINOSO	1	
98	2014-11-24 00:48:02.443-05	1	23	11	RELOJ DIGITAL	1	
99	2014-11-24 00:48:49.822-05	1	37	4	CERRAMIENTO	1	
100	2014-11-24 00:49:09.921-05	1	37	8	CONST. O CASA GUARDIA	1	
101	2014-11-24 00:49:23.259-05	1	37	10	CONST. O CASA GUARDIA	1	
102	2014-11-24 00:49:31.371-05	1	37	5	EN LA CAÑA	1	
103	2014-11-24 00:49:40.313-05	1	37	1	PARED FRONTAL	1	
104	2014-11-24 00:49:54.967-05	1	37	3	PARED LATERAL DER.	1	
105	2014-11-24 00:50:06.811-05	1	37	2	PARED LATERAL IZQ.	1	
106	2014-11-24 00:50:12.566-05	1	37	12	POSTE	1	
107	2014-11-24 00:50:22.08-05	1	37	6	TABLERO METALICO	1	
108	2014-11-24 00:50:32.8-05	1	37	7	ZAGUAN O PORTAL	1	
109	2014-11-24 00:51:02.656-05	1	27	AD	ADOSADA	1	
110	2014-11-24 00:51:11.069-05	1	27	AE	AEREA	1	
111	2014-11-24 00:51:18.51-05	1	27	AH	ANTIHURTO	1	
112	2014-11-24 00:51:28.049-05	1	27	SU	SUBTERRANEA	1	
113	2014-11-24 00:53:04.856-05	1	25	13	1x1/0(2)	1	
114	2014-11-24 00:53:20.456-05	1	25	10	1x2(4)	1	
115	2014-11-24 00:53:50.445-05	1	25	16	1x2/0(1/0)	1	
116	2014-11-24 00:54:15.223-05	1	25	19	1x3/0(2/0)	1	
117	2014-11-24 00:54:35.064-05	1	25	7	1x4(4)	1	
118	2014-11-24 00:54:50.167-05	1	25	4	1x6(6)	1	
119	2014-11-24 00:55:03.351-05	1	25	1	1x8(8)	1	
120	2014-11-24 00:55:29.543-05	1	25	17	2x1/0(2)	1	
121	2014-11-24 00:56:29.788-05	1	25	14	2x1/0(2)	2	Modificado/a id.
122	2014-11-24 00:56:58.145-05	1	25	11	2x2(4)	1	
123	2014-11-24 00:58:27.95-05	1	25	17	2x2/0(1/0)	2	Modificado/a descripcion.
124	2014-11-24 00:59:14.903-05	1	25	20	2x3/0(2/0)	1	
125	2014-11-24 00:59:27.087-05	1	25	8	2x4(4)	1	
126	2014-11-24 00:59:45.548-05	1	25	5	2x6(6)	1	
127	2014-11-24 00:59:57.802-05	1	25	2	2x8(8)	1	
128	2014-11-24 01:00:15.984-05	1	25	15	3x1/0(2)	1	
129	2014-11-24 01:00:29.628-05	1	25	12	3x2(4)	1	
130	2014-11-24 01:00:54.597-05	1	25	18	3x2/0(1/0)	1	
131	2014-11-24 01:01:24.113-05	1	25	21	3x3/0(2/0)	1	
132	2014-11-24 01:01:38.189-05	1	25	9	3x4(4)	1	
133	2014-11-24 01:01:47.578-05	1	25	6	3x6(6)	1	
134	2014-11-24 01:02:14.935-05	1	25	3	3x8(8)	1	
135	2014-11-24 01:02:58.075-05	1	24	D	DEFINITIVA	1	
136	2014-11-24 01:03:06.992-05	1	24	E	EXTENSION	1	
137	2014-11-24 01:03:15.546-05	1	24	P	PROVISIONAL	1	
138	2014-11-24 01:20:39.26-05	1	36	12M	MONOF. DOS HILOS	1	
139	2014-11-24 01:21:08.079-05	1	36	13M	MONOF. 3 HILOS	1	
140	2014-11-24 01:21:35.354-05	1	36	12B	MONOFASICO 2 HILOS	1	
141	2014-11-24 01:22:01.218-05	1	36	13B	MONOFASICO 3 HILOS	1	
142	2014-11-24 01:22:34.417-05	1	36	34A	TRIFASICO ALTA T.	1	
143	2014-11-24 01:23:02.311-05	1	36	34B	TRIFASICO BAJA T.	1	
144	2014-11-24 01:23:26.705-05	1	36	34M	TRIFASICO MEDIA T.	1	
145	2014-11-24 01:25:33.95-05	1	29	1	ALUMBRADO PUBLICO	1	
146	2014-11-24 01:25:52.002-05	1	29	2	ASISTENCIA SOCIAL	1	
147	2014-11-24 01:26:07.778-05	1	29	3	AUTOCONSUMO	1	
148	2014-11-24 01:26:40.249-05	1	29	4	BENEFICIO PUBLICO	1	
149	2014-11-24 01:26:52.875-05	1	29	5	BOMBEO DE AGUA	1	
150	2014-11-24 01:27:09.785-05	1	29	6	COMERCIAL	1	
151	2014-11-24 01:27:22.931-05	1	29	7	CULTO RELIGIOSO	1	
152	2014-11-24 01:27:33.487-05	1	29	8	ENTIDAD MUNICIPAL	1	
153	2014-11-24 01:27:45.527-05	1	29	9	ENTIDAD OFICIAL	1	
154	2014-11-24 01:27:55.724-05	1	29	13	ESCENARIO DEPORTIVO	1	
155	2014-11-24 01:28:18.345-05	1	29	10	INDUSTRIAL	1	
156	2014-11-24 01:28:27.569-05	1	29	11	LOCAL DEPORTIVO	1	
157	2014-11-24 01:28:35.99-05	1	29	12	RESIDENCIAL	1	
158	2014-11-24 01:36:14.288-05	1	30	1	RESIDENCIAL	1	
159	2014-11-24 01:38:05.311-05	1	30	2	RESIDENCIAL PEQUEÑO NEGOCIO	1	
160	2014-11-24 01:38:49.601-05	1	30	3	TIENDA-VIVIENDA	1	
161	2014-11-24 01:39:10.691-05	1	30	4	ZAPATERIA-VIVIENDA	1	
162	2014-11-24 01:40:33.726-05	1	30	2	RESIDENCIAL PEQUEÑO NEGOCIO	2	Modificado/a descripcion.
163	2014-11-24 01:40:48.511-05	1	30	1	RESIDENCIAL  	2	Modificado/a descripcion.
164	2014-11-24 01:44:34.077-05	1	31	ESP-65	ELECTRÓNICO 1F2C ACTIVA Y DEMANDA	1	
165	2014-11-24 01:45:24.475-05	1	31	ESP-70	ELECTRONICO 1F2C, A1R-L 3S CL 20	1	
166	2014-11-24 01:45:56.382-05	1	31	ESP-80	ELECTRONICO 1F2C, A1R 2S CL 200	1	
167	2014-11-24 01:46:35.185-05	1	31	ESP-90	ELECTRONICO 1F3C, A1R 4S, CL 20	1	
168	2014-11-24 01:46:47.835-05	1	31	ESP-80	ELECTRONICO 1F3C, A1R 2S CL 200	2	Modificado/a descripcion.
169	2014-11-24 01:48:09.966-05	1	31	ESP-10	ELECTRONICO 1F3C, A1R, 4SPLUS, CL 20	1	
170	2014-11-24 01:49:23.091-05	1	31	ESP-100	ELECTRONICO 1F3C, A1R, 4SPLUS, CL 20	2	Modificado/a id.
171	2014-11-24 01:49:43.959-05	1	31	ESP-10	ELECTRONICO 1F3C, A1R, 4SPLUS, CL 20	3	
172	2014-11-24 01:50:34.352-05	1	31	ESP-105	BIFASICO ELECTRÓ. ACT, REAC Y DEMAN	1	
173	2014-11-24 01:51:51.423-05	1	31	ESP-110	ELECTRONICO 3F3C, A1R-AL, 5S CL20	1	
174	2014-11-24 01:53:05.303-05	1	31	ESP-120	ELECTRONICO 3F3C, A1R-AL, 5S PLUS,CL 20	1	
175	2014-11-24 01:53:58.091-05	1	31	ESP-130	ELECTRONICO 3F4C, ACTIVA Y REACTIVA	1	
176	2014-11-24 01:54:54.663-05	1	31	ESP-140	ELECTRONICO 3F4C,ACT. REAC. Y DEMANDA	1	
177	2014-11-24 01:56:56.025-05	1	31	ESP-150	ELECTRONICO 3F4C, A1D, 16A, CL 100	1	
178	2014-11-24 01:58:02.711-05	1	31	ESP-160	ELECTRONICO 3F4C, A1R, 16A, CL 100	1	
179	2014-11-24 01:59:15.357-05	1	31	ESP-170	ELECTRONICO 3F4C, A1R-LQ,16APLUS, CL 100	1	
180	2014-11-24 02:00:09.128-05	1	31	ESP-180	ELECTRONICO 3F4C, A1R, 16S, CL 200	1	
181	2014-11-24 02:01:01.584-05	1	31	ESP-190	ELECTRONICO 3F4C,A1R-LQ, 16S, PLUS,CL200	1	
182	2014-11-24 02:01:54.964-05	1	31	ESP-200	ELECTRONICO 3F4C,A1R-LQ, 10A, CL20	1	
183	2014-11-24 02:02:50.478-05	1	31	ESP-210	ELECTRONICO 3F4C,A1R-LQ,10A, PLUS,CL20	1	
184	2014-11-24 02:05:50.122-05	1	31	ESP-220	ELECTRONICO 3F4C,A1R, 9S, CL 20	1	
185	2014-11-24 02:06:44.739-05	1	31	ESP-230	ELECTRONICO 3F4C, A1R-AL, 9S, CL 20	1	
186	2014-11-24 02:07:06.821-05	1	31	ESP-240	ELECTRONICO 3F4C, A1R-AL, 5A, CL 20	1	
187	2014-11-24 02:07:51.097-05	1	31	NOR-10	MONOFASICO DOS CONDUCTORES	1	
188	2014-11-24 02:08:09.855-05	1	31	NOR-20	MONOFASICO TRES CONDUCTORES	1	
189	2014-11-24 02:08:30.71-05	1	31	NOR-25	BIFASICO TRES CONDUCTORES	1	
190	2014-11-24 02:08:54.886-05	1	31	NOR-30	TRIFASICO CUATRO CONDUCTORES	1	
191	2014-11-24 02:09:33.755-05	1	31	NOR-40	TRIFASICO 3F4C, CON REACTIVA	1	
192	2014-11-24 02:10:19.335-05	1	31	NOR-50	TRIFASICO 3F4C, CON REACTIVA INDIRECTO	1	
193	2014-11-24 02:10:59.637-05	1	31	NOR-60	TRIFASICO 3F4C,REACT. Y REG. DEMANDA	1	
194	2014-11-24 02:13:40.5-05	1	32	1	CARGA INSTALADA ENTRE 0 Y 0,50 KVA	1	
195	2014-11-24 02:14:00.065-05	1	32	2	CARGA INSTALADA ENTRE 0,51 Y 1	1	
196	2014-11-24 02:14:19.632-05	1	32	2	CARGA INSTALADA ENTRE 0,51 Y 1 KVA	2	Modificado/a descripcion.
197	2014-11-24 02:14:46.82-05	1	32	3	CARGA INSTALADA ENTRE 1,01 Y 2 KVA	1	
198	2014-11-24 02:15:14.682-05	1	32	4	CARGA INSTALADA ENTRE 2.01 Y 3 KVA	1	
199	2014-11-24 02:15:32.132-05	1	32	5	CARGA INSTALADA ENTRE 3,01 Y 4 KVA	1	
200	2014-11-24 02:16:14.829-05	1	32	6	CARGA INSTALADA ENTRE 4,01 Y 5 KVA	1	
201	2014-11-24 02:16:36.916-05	1	32	7	CARGA INSTALADA ENTRE 5,01 Y 6 KVA	1	
202	2014-11-24 02:17:07.345-05	1	32	8	CARGA INSTALADA ENTRE 6,01 Y 7 KVA	1	
203	2014-11-24 02:17:30.171-05	1	32	9	CARGA INSTALADA ENTRE 7,01 Y 8 KVA	1	
204	2014-11-24 02:17:49.916-05	1	32	10	CARGA INSTALADA ENTRE 8,01 Y 10 KVA	1	
205	2014-11-24 02:19:18.339-05	1	33	1	NORMAL	1	
206	2014-11-24 02:21:02.836-05	1	33	2	CARGA INSTALADA ENTRE 0 Y 2 KVA	1	
207	2014-11-24 02:21:21.84-05	1	33	11	CARGA INSTALADA ENTRE 0 Y 2 KVA	2	Modificado/a id.
208	2014-11-24 02:21:49.145-05	1	33	2	CARGA INSTALADA ENTRE 0 Y 2 KVA	3	
209	2014-11-24 02:22:07.074-05	1	33	12	CARGA INSTALADA ENTRE 3 Y 4 KVA	1	
210	2014-11-24 02:22:19.183-05	1	33	13	CARGA INSTALADA ENTRE 5 Y 7 KVA	1	
211	2014-11-24 02:22:33.689-05	1	33	14	CARGA INSTALADA ENTRE 7 Y 10 KVA	1	
212	2014-11-24 02:22:55.122-05	1	33	15	CARGA INSTALADA ENTRE 11 Y 15 KVA	1	
213	2014-11-24 02:23:08.256-05	1	33	16	CARGA INSTALADA ENTRE 16 Y 20 KVA	1	
214	2014-11-24 02:23:22.954-05	1	33	17	CARGA INSTALADA ENTRE 20 Y 30 KVA	1	
215	2014-11-24 02:23:49.764-05	1	33	18	CARGA INSTALADA ENTRE 31 Y 40 KVA	1	
216	2014-11-24 02:24:41.611-05	1	33	19	CARGA INSTALADA ENTRE 31 Y 50 KVA	1	
217	2014-11-24 02:24:57.741-05	1	33	19	CARGA INSTALADA ENTRE 41 Y 50 KVA	2	Modificado/a descripcion.
218	2014-11-24 02:45:38.662-05	1	33	20	CARGA INSTALADA ENTRE 51 Y 70 KVA	1	
219	2014-11-24 02:45:55.648-05	1	33	21	CARGA INSTALADA ENTRE 71 Y 100 KVA	1	
220	2014-11-24 02:46:12.374-05	1	33	22	CARGA INSTALADA ENTRE 101 Y 150 KVA	1	
221	2014-11-24 02:46:46.797-05	1	33	23	CARGA INSTALADA ENTRE 151 Y 200 KVA	1	
222	2014-11-24 02:47:09.34-05	1	33	24	CARGA INSTALADA ENTRE 201 Y 300 KVA	1	
223	2014-11-24 02:47:23.003-05	1	33	25	CARGA INSTALADA ENTRE 301 Y 400 KVA	1	
224	2014-11-24 02:47:42.366-05	1	33	26	CARGA INSTALADA ENTRE 401 Y 500 KVA	1	
225	2014-11-24 02:48:04.587-05	1	33	27	CARGA INSTALADA ENTRE 501 Y 650 KVA	1	
226	2014-11-24 02:48:31.895-05	1	33	28	CARGA INSTALADA ENTRE 651 Y 800 KVA	1	
227	2014-11-24 02:48:53.053-05	1	33	29	CARGA INSTALADA ENTRE 801 Y 1000 KVA	1	
228	2014-11-24 02:50:10.098-05	1	33	30	CARGA INSTALADA ENTRE 1001 Y MAS	1	
229	2014-11-24 02:56:43.009-05	1	8	7	EL ORO	1	
230	2014-11-24 02:56:54.755-05	1	8	3	AZUAY	1	
231	2014-11-24 02:57:05.218-05	1	8	9	GUAYAS	1	
232	2014-11-24 02:59:07.287-05	1	9	2	MACHALA	1	
233	2014-11-24 02:59:44.26-05	1	9	3	SANTA ROSA	1	
234	2014-11-24 03:01:08.041-05	1	9	4	ARENILLAS	1	
235	2014-11-24 03:02:32.898-05	1	8	1	AZUAY	2	Modificado/a id.
236	2014-11-24 03:02:52.237-05	1	8	3	AZUAY	3	
237	2014-11-24 03:04:23.439-05	1	9	5	PUCARA	1	
238	2014-11-24 03:04:48.411-05	1	9	6	CAMILO PONCE ENRIQUE	1	
239	2014-11-24 03:05:02.418-05	1	9	7	MOLLETURO	1	
240	2014-11-24 03:05:21.703-05	1	9	8	SANTA ISABEL	1	
241	2014-11-24 03:06:20.478-05	1	9	9	ARENILLAS	1	
242	2014-11-24 03:06:36.648-05	1	9	10	ATAHUALPA	1	
243	2014-11-24 03:06:44.623-05	1	9	11	BALSAS	1	
244	2014-11-24 03:06:53.709-05	1	9	12	CHILLA	1	
245	2014-11-24 03:07:00.343-05	1	9	13	EL GUABO	1	
246	2014-11-24 03:07:13.809-05	1	9	14	HUAQUILLAS	1	
247	2014-11-24 03:07:21.825-05	1	9	15	MARCABELI	1	
248	2014-11-24 03:07:34.144-05	1	9	16	PASAJE	1	
249	2014-11-24 03:07:40.051-05	1	9	17	PIÑAS	1	
250	2014-11-24 03:08:19.518-05	1	9	18	PORTOVELO	1	
251	2014-11-24 03:08:29.936-05	1	9	19	ZARUMA	1	
252	2014-11-24 03:08:36.781-05	1	9	20	LAS LAJAS	1	
253	2014-11-24 03:09:04.443-05	1	9	4	ARENILLAS	3	
254	2014-11-24 03:09:42.259-05	1	9	21	GUAYAQUIL	1	
255	2014-11-24 03:09:49.637-05	1	9	22	BALAO	1	
256	2014-11-24 03:09:57.633-05	1	9	23	TENGUEL	1	
257	2014-11-24 03:10:10.415-05	1	9	24	NARANJAL	1	
258	2014-11-24 03:11:39.771-05	1	10	1	CABECERA CANTONAL	1	
259	2014-11-24 03:11:58.547-05	1	10	2	LAS PALMAS	1	
260	2014-11-24 03:12:08.126-05	1	10	3	PUCARA	1	
261	2014-11-24 03:12:32.444-05	1	10	4	SAN RAFAEL DE SHARUG	1	
262	2014-11-24 03:12:48.213-05	1	10	5	SANTA CECILIA 2 	1	
263	2014-11-24 03:12:58.536-05	1	10	6	SARAYUNGA	1	
264	2014-11-24 03:13:07.518-05	1	10	7	TRES BANDERAS	1	
265	2014-11-24 03:14:08.424-05	1	10	8	PONCE ENRIQUEZ	1	
266	2014-11-24 03:14:52.93-05	1	10	9	MOLLETURO	1	
267	2014-11-24 03:17:03.967-05	1	10	10	SANTA ISABEL	1	
268	2014-11-24 03:17:33.528-05	1	10	11	*EL CAMBIO	1	
269	2014-11-24 03:17:50.022-05	1	10	12	EL CAMBIO	1	
270	2014-11-24 03:17:59.211-05	1	10	13	EL RETIRO	1	
271	2014-11-24 03:18:13.738-05	1	10	14	JAMBELI.	1	
272	2014-11-24 03:18:26.673-05	1	10	15	JUBONES	1	
273	2014-11-24 03:18:39.409-05	1	10	16	LA PROVIDENCIA	1	
274	2014-11-24 03:18:48.821-05	1	10	17	MACHALA	1	
275	2014-11-24 03:19:18.234-05	1	10	18	MACHALA, CABECERA CA	1	
276	2014-11-24 03:19:34.749-05	1	10	19	NUEVE DE MAYO	1	
277	2014-11-24 03:19:51.922-05	1	10	20	PUERTO BOLIVAR	1	
278	2014-11-24 03:22:18.183-05	1	10	21	*LA LIBERTAD	1	
279	2014-11-24 03:23:08.613-05	1	10	22	*LAS LAJAS (CAB. EN	1	
280	2014-11-24 03:23:31.369-05	1	10	23	ARENILLAS, CABECERA	1	
281	2014-11-24 03:23:43.412-05	1	10	24	CARCABON	1	
282	2014-11-24 03:23:54.4-05	1	10	25	CHACRAS	1	
283	2014-11-24 03:24:11.624-05	1	10	26	PALMARES	1	
284	2014-11-24 03:25:06.194-05	1	10	27	AYAPAMBA	1	
285	2014-11-24 03:25:20.668-05	1	10	28	CERRO AZUL	1	
286	2014-11-24 03:25:40.174-05	1	10	29	CORDONCILLO	1	
287	2014-11-24 03:26:01.787-05	1	10	30	MILAGRO	1	
288	2014-11-24 03:26:44.297-05	1	10	31	PACCHA, CABECERA CAN	1	
289	2014-11-24 03:27:02.674-05	1	10	32	SAN JOSE	1	
290	2014-11-24 03:27:20.392-05	1	10	33	SAN JOSE DE CERRO AZ	1	
291	2014-11-24 03:28:10.501-05	1	10	34	BALSAS, CABECERA CAN	1	
292	2014-11-24 03:28:25.254-05	1	10	35	BELLAMARIA	1	
293	2014-11-24 03:29:27.664-05	1	10	36	CHILLA, CABECERA CAN	1	
294	2014-11-24 03:29:38.214-05	1	10	37	SAN RAFAEL	1	
295	2014-11-24 03:29:59.936-05	1	10	38	DUMARI	1	
296	2014-11-24 03:30:58.287-05	1	10	39	BARBONES (SUCRE)	1	
297	2014-11-24 03:31:27.022-05	1	10	40	EL GUABO, CABECERA C	1	
298	2014-11-24 03:31:47.662-05	1	10	41	LA IBERIA	1	
299	2014-11-24 03:32:05.009-05	1	10	42	RIO BONITO	1	
300	2014-11-24 03:32:58.373-05	1	10	43	TENDALES (CAB.EN PUE	1	
301	2014-11-24 14:46:25.859-05	1	10	44	CARCA 1	1	
302	2014-11-24 14:46:55.964-05	1	10	45	CHACRAS1	1	
303	2014-11-24 14:47:04.004-05	1	10	46	ECUADOR	1	
304	2014-11-24 14:47:20.763-05	1	10	47	EL PARAISO	1	
305	2014-11-24 14:47:35.145-05	1	10	48	HUALTACO	1	
306	2014-11-24 14:47:56.12-05	1	10	49	HUAQUILLAS, CABECERA	1	
307	2014-11-24 14:48:11.069-05	1	10	50	JAMBELI	1	
308	2014-11-24 14:48:20.857-05	1	10	51	JAMBELI NO	1	
309	2014-11-24 14:48:30.872-05	1	10	52	MILTON REYES	1	
310	2014-11-24 14:48:41.923-05	1	10	53	UNION LOJANA	1	
311	2014-11-24 14:49:49.16-05	1	10	54	ZONA RURAL ARENILLAS	1	
312	2014-11-24 14:50:44.623-05	1	10	55	EL INGENIO	1	
313	2014-11-24 14:51:02.219-05	1	10	56	MARCABELI, CABECERA	1	
314	2014-11-24 14:51:44.607-05	1	10	57	BOLIBAR	1	
315	2014-11-24 14:51:56.005-05	1	10	58	BUENAVISTA	1	
316	2014-11-24 14:52:07.085-05	1	10	59	CAÑAQUEMADA	1	
317	2014-11-24 14:52:16.197-05	1	10	60	CASACAY	1	
318	2014-11-24 14:52:24.913-05	1	10	61	CERRO AZUL	1	
319	2014-11-24 14:52:32.915-05	1	10	62	LA PEAÑA	1	
320	2014-11-24 14:52:45.466-05	1	10	63	LOMA DE FRANCO	1	
321	2014-11-24 14:53:00.372-05	1	10	64	OCHOA LEON (MATRIZ)	1	
322	2014-11-24 14:53:18.13-05	1	10	65	PASAJE, CABECERA CAN	1	
323	2014-11-24 14:53:31.268-05	1	10	66	PROGRESO	1	
324	2014-11-24 14:54:30.59-05	1	10	67	SANTA CECILIA	1	
325	2014-11-24 14:54:41.167-05	1	10	68	TRES CERRITOS	1	
326	2014-11-24 14:54:57.905-05	1	10	69	UZHCURRUMI	1	
327	2014-11-24 14:55:49.589-05	1	10	70	CAPIRO (CAB. EN LA C	1	
328	2014-11-24 14:56:02.027-05	1	10	71	LA BOCANA	1	
329	2014-11-24 14:56:13.676-05	1	10	72	LA MATRIZ	1	
330	2014-11-24 14:56:22.657-05	1	10	73	LA SUSAYA	1	
331	2014-11-24 14:56:45.898-05	1	10	74	MOROMORO (CAB. EN EL	1	
332	2014-11-24 14:56:58.589-05	1	10	75	PIÑAS GRANDE	1	
333	2014-11-24 14:57:23.09-05	1	10	76	PIÑAS, CABECERA CANT	1	
334	2014-11-24 14:58:14.182-05	1	10	77	PIEDRA BLANCA	1	
335	2014-11-24 14:58:24.927-05	1	10	78	PIEDRAS	1	
336	2014-11-24 14:59:04.549-05	1	10	79	SAN ROQUE (AMBROSIO	1	
337	2014-11-24 14:59:15.332-05	1	10	80	SARACAY	1	
338	2014-11-24 15:00:16.333-05	1	10	81	CURTINCAPA	1	
339	2014-11-24 15:00:26.641-05	1	10	82	MORALES	1	
340	2014-11-24 15:00:45.144-05	1	10	83	PORTOVELO, CABECERA	1	
341	2014-11-24 15:00:52.849-05	1	10	84	SALATI	1	
342	2014-11-24 15:01:27.235-05	1	10	85	BELLAMARIA	1	
343	2014-11-24 15:01:36.56-05	1	10	86	BELLAVISTA	1	
344	2014-11-24 15:01:43.785-05	1	10	87	JAMBELI	1	
345	2014-11-24 15:01:59.562-05	1	10	88	JAMBELI (SATELITE)	1	
346	2014-11-24 15:02:12.359-05	1	10	89	JUMON (SATELITE)	1	
347	2014-11-24 15:02:20.376-05	1	10	90	LA AVANZADA	1	
348	2014-11-24 15:02:33.384-05	1	10	91	NUEVO SANTA ROSA	1	
349	2014-11-24 15:02:40.923-05	1	10	92	PUERTO JELI	1	
350	2014-11-24 15:02:51.717-05	1	10	93	SAN ANTONIO	1	
351	2014-11-24 15:03:01.502-05	1	10	94	SANTA ROSA	1	
352	2014-11-24 15:04:39.341-05	1	10	95	SANTA ROSA, CABECERA	1	
353	2014-11-24 15:04:45.232-05	1	10	96	TORATA	1	
354	2014-11-24 15:04:53.852-05	1	10	97	VICTORIA	1	
355	2014-11-24 15:06:18.462-05	1	10	98	ABAÑIN	1	
356	2014-11-24 15:06:26.78-05	1	10	99	ARCAPAMBA	1	
357	2014-11-24 15:06:35.129-05	1	10	100	GUANAZAN	1	
358	2014-11-24 15:06:59.271-05	1	10	101	GUISHAGUIÑA	1	
359	2014-11-24 15:07:09.911-05	1	10	102	HUERTAS	1	
360	2014-11-24 15:07:17.269-05	1	10	103	MALVAS	1	
361	2014-11-24 15:07:28.298-05	1	10	104	MULUNCAY	1	
362	2014-11-24 15:07:39.272-05	1	10	105	SALVIAS	1	
363	2014-11-24 15:07:47.016-05	1	10	106	SINSAO	1	
364	2014-11-24 15:07:56.506-05	1	10	107	ZARUMA CABECERA	1	
365	2014-11-24 15:09:21.475-05	1	10	108	EL PARAISO	1	
366	2014-11-24 15:09:30.57-05	1	10	109	EL PROGRESO	1	
367	2014-11-24 15:09:43.927-05	1	10	110	LA LIBERTAD	1	
368	2014-11-24 15:09:53.076-05	1	10	111	LA VICTORIA	1	
369	2014-11-24 15:10:12.342-05	1	10	112	LA VICTORIA, CABECER	1	
370	2014-11-24 15:10:29.434-05	1	10	113	PLATANILLOS	1	
371	2014-11-24 15:10:41.388-05	1	10	114	SAN ISIDRO	1	
372	2014-11-24 15:10:52.985-05	1	10	115	VALLE HERMOSO	1	
373	2014-11-24 15:12:48.691-05	1	10	116	TENGUEL	1	
374	2014-11-24 15:13:49.904-05	1	9	25	BALAO	1	
375	2014-11-24 15:13:56.87-05	1	10	117	BALAO, CABECERA CANT	1	
376	2014-11-24 15:14:38.844-05	1	10	118	PARROQUIA TENGUEL	1	
377	2014-11-24 15:15:14.265-05	1	10	119	NARANJAL,CABECERA CA	1	
378	2014-11-24 16:22:47.286-05	1	21	AV	AVENIDA	1	
379	2014-11-24 16:25:34.374-05	1	20	1	AV. ING. DAVILA	1	
380	2014-11-24 16:27:00.349-05	1	17	3	ARENILLAS, CABECERA; AV. ING. DAVILA y None; Urb: None, Cas: None	1	
381	2014-11-24 16:28:56.23-05	1	20	2	AV. TENIENTE CORDOVEZ	1	
382	2014-11-24 16:30:01.328-05	1	17	3	ARENILLAS, CABECERA; AV. ING. DAVILA y None; Urb: None, Cas: None	3	
383	2014-11-24 16:37:11.115-05	1	20	3	MIGUEL RIVAS 	1	
384	2014-11-24 16:37:42.453-05	1	20	4	PORTOVELO 	1	
385	2014-11-24 16:38:24.338-05	1	20	5	RAUL FRIAS AGUIRRE 	1	
386	2014-11-24 16:38:51.545-05	1	21	CA	CALLE	1	
387	2014-11-24 16:38:58.033-05	1	20	6	ABAD HUMBERTO	1	
\.


--
-- TOC entry 2683 (class 0 OID 0)
-- Dependencies: 178
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 387, true);


--
-- TOC entry 2544 (class 0 OID 27562)
-- Dependencies: 179
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_content_type (id, name, app_label, model) FROM stdin;
1	permission	auth	permission
2	group	auth	group
3	user	auth	user
4	content type	contenttypes	contenttype
5	session	sessions	session
6	log entry	admin	logentry
7	Registro de Búsqueda	busquedas	vitacorabusquedas
8	provincia	ingresos	provincia
9	canton	ingresos	canton
10	parroquia	ingresos	parroquia
11	sector	ingresos	sector
12	ruta	ingresos	ruta
13	Geocódigo	ingresos	secuencia
14	cliente	ingresos	cliente
15	Detalle Cliente-Medidor	ingresos	detalleclientemedidor
16	detalle cliente referencia	ingresos	detalleclientereferencia
17	Ubicación	ingresos	ubicacion
18	caserio	ingresos	caserio
19	Urbanización	ingresos	urbanizacion
20	calle	ingresos	calle
21	tipo calle	ingresos	tipocalle
22	Actividad	ingresos	actividad
23	Tipo de Construcción	ingresos	tipodeconstruccion
24	Clase de Red	ingresos	clasered
25	Calibre de Red	ingresos	calibredelared
26	Estado de una Instalación	ingresos	estadodeunainstalacion
27	Tipo de Acometida o Red	ingresos	tipodeacometidared
28	Uso de Energía	ingresos	usodeenergia
29	Uso General del Inmueble	ingresos	usogeneraldelinmueble
30	Uso Específico del Inmueble	ingresos	usoespecificodelinmueble
31	Modelo de Medidor	ingresos	modelodemedidor
32	Forma de Conexión	ingresos	formadeconexion
33	demanda	ingresos	demanda
34	Motivo para Solicitud	ingresos	motivoparasolicitud
35	Tipo de Solicitud	ingresos	tipodesolicitud
36	Tipo de Servicio	ingresos	tipodeservicio
37	Ubicación del Medidor	ingresos	ubicaciondelmedidor
38	cuadrilla	ingresos	cuadrilla
39	empleado	ingresos	empleado
40	instalador	ingresos	instalador
41	material de actividad	ingresos	materialdeactividad
42	Rubro de Actividad	ingresos	detalledeactividad
43	Foto	ingresos	foto
44	Nivel Socioeconómico	ingresos	nivelsocieconomico
45	contrato	inventario	contrato
46	marca	inventario	marca
47	medidor	inventario	medidor
48	sello	inventario	sello
49	subtipo de material	inventario	subtipodematerial
50	tipo de material	inventario	tipodematerial
51	material	inventario	material
52	rango de material	inventario	rangodematerial
53	detalle material contrato	inventario	detallematerialcontrato
54	servicio	inventario	servicio
55	rubro	inventario	rubro
56	detalle rubro	inventario	detallerubro
57	Usuario en Sico	usuarios	usuariosico
\.


--
-- TOC entry 2684 (class 0 OID 0)
-- Dependencies: 180
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_content_type_id_seq', 57, true);


--
-- TOC entry 2546 (class 0 OID 27567)
-- Dependencies: 181
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
ta9go2k6vab4v1fwjf9vaoiwqqyggpfi	MzZhN2E3OGUxM2JmODk2NTkxNmQwMmFhNzZhYmZjMzFmZThiOGE3NTqAAn1xAShVCmxhc3RfdG91Y2hjZGF0ZXRpbWUKZGF0ZXRpbWUKcQJVCgfeCxgDIDsINZCFUnEDVRJfYXV0aF91c2VyX2JhY2tlbmRVKWRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kVQ1fYXV0aF91c2VyX2lkSwF1Lg==	2014-12-08 03:32:59.545-05
ln91vvekt2uctju5qboj3dp664fjhcd4	Njk1MzIxMmUwMjA5YmI1OTIwNWVhYjljMDFkNzAwYTdjMzBhZDViMjqAAn1xAS4=	2014-12-07 22:50:51.902-05
ik9qnsc6u753uqjozowi4ap9p1fx27q9	YTgxMzg1OTJiYjYzNDY2YjdhYjBmYzEzYjViYjk1NmMwZDFlZTgwNjqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH3gsYEQQKDrG4hVJxBHMu	2014-12-08 17:04:10.979-05
\.


--
-- TOC entry 2547 (class 0 OID 27573)
-- Dependencies: 182
-- Data for Name: ingresos_actividad; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_actividad (id, "numeroDeSolicitud", cliente_id, "tipoDeConstruccion_id", "materialDeRed", instalador_id, "ubicacionDelMedidor_id", "claseRed_id", "nivelSocieconomico_id", "calibreDeLaRed_id", "estadoDeLaInstalacion_id", "tipoDeAcometidaRed_id", "fechaDeActividad", "usoDeEnergia_id", "usoEspecificoDelInmueble_id", "formaDeConexion_id", demanda_id, "motivoDeSolicitud_id", "tipoDeSolicitud_id") FROM stdin;
\.


--
-- TOC entry 2685 (class 0 OID 0)
-- Dependencies: 183
-- Name: ingresos_actividad_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ingresos_actividad_id_seq', 1, false);


--
-- TOC entry 2549 (class 0 OID 27578)
-- Dependencies: 184
-- Data for Name: ingresos_calibredelared; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_calibredelared (id, descripcion) FROM stdin;
13	1x1/0(2)
10	1x2(4)
16	1x2/0(1/0)
19	1x3/0(2/0)
7	1x4(4)
4	1x6(6)
1	1x8(8)
14	2x1/0(2)
11	2x2(4)
17	2x2/0(1/0)
20	2x3/0(2/0)
8	2x4(4)
5	2x6(6)
2	2x8(8)
15	3x1/0(2)
12	3x2(4)
18	3x2/0(1/0)
21	3x3/0(2/0)
9	3x4(4)
6	3x6(6)
3	3x8(8)
\.


--
-- TOC entry 2550 (class 0 OID 27582)
-- Dependencies: 185
-- Data for Name: ingresos_calle; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_calle (id, descripcion1, "tipoDeCalle_id", "codigoDeCalle", descripcion2) FROM stdin;
1	AV. ING. DAVILA	AV	A04060	
2	AV. TENIENTE CORDOVEZ	AV	CORD01	
3	MIGUEL RIVAS	AV	MIG011	
4	PORTOVELO	AV	P04460	
5	RAUL FRIAS AGUIRRE	AV	RAFR01	
6	ABAD	CA	ABA001	HUMBERTO
\.


--
-- TOC entry 2686 (class 0 OID 0)
-- Dependencies: 186
-- Name: ingresos_calle_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ingresos_calle_id_seq', 6, true);


--
-- TOC entry 2552 (class 0 OID 27587)
-- Dependencies: 187
-- Data for Name: ingresos_canton; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_canton (id, num, descripcion, provincia_id) FROM stdin;
2	1	MACHALA	7
3	12	SANTA ROSA	7
5	6	PUCARA	1
6	15	CAMILO PONCE ENRIQUE	1
7	16	MOLLETURO	1
8	17	SANTA ISABEL	1
9	2	ARENILLAS	7
10	3	ATAHUALPA	7
11	4	BALSAS	7
12	5	CHILLA	7
13	6	EL GUABO	7
14	7	HUAQUILLAS	7
15	8	MARCABELI	7
16	9	PASAJE	7
17	10	PIÑAS	7
18	11	PORTOVELO	7
19	13	ZARUMA	7
20	14	LAS LAJAS	7
21	1	GUAYAQUIL	9
22	3	BALAO	9
23	4	TENGUEL	9
24	11	NARANJAL	9
25	3	BALAO	9
\.


--
-- TOC entry 2687 (class 0 OID 0)
-- Dependencies: 188
-- Name: ingresos_canton_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ingresos_canton_id_seq', 25, true);


--
-- TOC entry 2554 (class 0 OID 27593)
-- Dependencies: 189
-- Data for Name: ingresos_caserio; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_caserio (id, descripcion) FROM stdin;
\.


--
-- TOC entry 2688 (class 0 OID 0)
-- Dependencies: 190
-- Name: ingresos_caserio_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ingresos_caserio_id_seq', 1, false);


--
-- TOC entry 2556 (class 0 OID 27598)
-- Dependencies: 191
-- Data for Name: ingresos_clasered; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_clasered (id, descripcion) FROM stdin;
D	DEFINITIVA
E	EXTENSION
P	PROVISIONAL
\.


--
-- TOC entry 2557 (class 0 OID 27601)
-- Dependencies: 192
-- Data for Name: ingresos_cliente; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_cliente (id, ci_ruc, cuenta, nombre, deuda, meses, geocodigo_id, "ubicacionGeografica_id", tipo, estado, telefono) FROM stdin;
\.


--
-- TOC entry 2689 (class 0 OID 0)
-- Dependencies: 193
-- Name: ingresos_cliente_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ingresos_cliente_id_seq', 1, false);


--
-- TOC entry 2559 (class 0 OID 27607)
-- Dependencies: 194
-- Data for Name: ingresos_cuadrilla; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_cuadrilla (id, nombre, observacion) FROM stdin;
\.


--
-- TOC entry 2690 (class 0 OID 0)
-- Dependencies: 195
-- Name: ingresos_cuadrilla_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ingresos_cuadrilla_id_seq', 1, false);


--
-- TOC entry 2561 (class 0 OID 27612)
-- Dependencies: 196
-- Data for Name: ingresos_demanda; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_demanda (id, descripcion) FROM stdin;
1	NORMAL
11	CARGA INSTALADA ENTRE 0 Y 2 KVA
12	CARGA INSTALADA ENTRE 3 Y 4 KVA
13	CARGA INSTALADA ENTRE 5 Y 7 KVA
14	CARGA INSTALADA ENTRE 7 Y 10 KVA
15	CARGA INSTALADA ENTRE 11 Y 15 KVA
16	CARGA INSTALADA ENTRE 16 Y 20 KVA
17	CARGA INSTALADA ENTRE 20 Y 30 KVA
18	CARGA INSTALADA ENTRE 31 Y 40 KVA
19	CARGA INSTALADA ENTRE 41 Y 50 KVA
20	CARGA INSTALADA ENTRE 51 Y 70 KVA
21	CARGA INSTALADA ENTRE 71 Y 100 KVA
22	CARGA INSTALADA ENTRE 101 Y 150 KVA
23	CARGA INSTALADA ENTRE 151 Y 200 KVA
24	CARGA INSTALADA ENTRE 201 Y 300 KVA
25	CARGA INSTALADA ENTRE 301 Y 400 KVA
26	CARGA INSTALADA ENTRE 401 Y 500 KVA
27	CARGA INSTALADA ENTRE 501 Y 650 KVA
28	CARGA INSTALADA ENTRE 651 Y 800 KVA
29	CARGA INSTALADA ENTRE 801 Y 1000 KVA
30	CARGA INSTALADA ENTRE 1001 Y MAS
\.


--
-- TOC entry 2562 (class 0 OID 27616)
-- Dependencies: 197
-- Data for Name: ingresos_detalleclientemedidor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_detalleclientemedidor (id, lectura_instalacion, lectura_desinstalacion, fecha_instalacion, fecha_desinstalacion, medidor_id, cliente_id, observacion) FROM stdin;
\.


--
-- TOC entry 2691 (class 0 OID 0)
-- Dependencies: 198
-- Name: ingresos_detalleclientemedidor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ingresos_detalleclientemedidor_id_seq', 1, false);


--
-- TOC entry 2564 (class 0 OID 27621)
-- Dependencies: 199
-- Data for Name: ingresos_detalleclientereferencia; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_detalleclientereferencia (id, cliente_id, referencia_id, "medidorDeReferencia", ubicacion_id) FROM stdin;
\.


--
-- TOC entry 2692 (class 0 OID 0)
-- Dependencies: 200
-- Name: ingresos_detalleclientereferencia_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ingresos_detalleclientereferencia_id_seq', 1, false);


--
-- TOC entry 2566 (class 0 OID 27626)
-- Dependencies: 201
-- Data for Name: ingresos_detalledeactividad; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_detalledeactividad (id, rubro_id, actividad_id) FROM stdin;
\.


--
-- TOC entry 2693 (class 0 OID 0)
-- Dependencies: 202
-- Name: ingresos_detalledeactividad_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ingresos_detalledeactividad_id_seq', 1, false);


--
-- TOC entry 2568 (class 0 OID 27631)
-- Dependencies: 203
-- Data for Name: ingresos_empleado; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_empleado (id, nombre, apellido, telefono, correo, observacion) FROM stdin;
\.


--
-- TOC entry 2694 (class 0 OID 0)
-- Dependencies: 204
-- Name: ingresos_empleado_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ingresos_empleado_id_seq', 1, false);


--
-- TOC entry 2570 (class 0 OID 27636)
-- Dependencies: 205
-- Data for Name: ingresos_estadodeunainstalacion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_estadodeunainstalacion (id, descripcion) FROM stdin;
1	ACEPTABLE
2	DEFICIENTE
3	REGULAR
4	SIN INSTALACION E.C.
\.


--
-- TOC entry 2571 (class 0 OID 27640)
-- Dependencies: 206
-- Data for Name: ingresos_formadeconexion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_formadeconexion (id, descripcion) FROM stdin;
1	CARGA INSTALADA ENTRE 0 Y 0,50 KVA
2	CARGA INSTALADA ENTRE 0,51 Y 1 KVA
3	CARGA INSTALADA ENTRE 1,01 Y 2 KVA
4	CARGA INSTALADA ENTRE 2.01 Y 3 KVA
5	CARGA INSTALADA ENTRE 3,01 Y 4 KVA
6	CARGA INSTALADA ENTRE 4,01 Y 5 KVA
7	CARGA INSTALADA ENTRE 5,01 Y 6 KVA
8	CARGA INSTALADA ENTRE 6,01 Y 7 KVA
9	CARGA INSTALADA ENTRE 7,01 Y 8 KVA
10	CARGA INSTALADA ENTRE 8,01 Y 10 KVA
\.


--
-- TOC entry 2572 (class 0 OID 27644)
-- Dependencies: 207
-- Data for Name: ingresos_foto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_foto (id, actividad_id, observacion, ruta) FROM stdin;
\.


--
-- TOC entry 2695 (class 0 OID 0)
-- Dependencies: 208
-- Name: ingresos_foto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ingresos_foto_id_seq', 1, false);


--
-- TOC entry 2574 (class 0 OID 27649)
-- Dependencies: 209
-- Data for Name: ingresos_instalador; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_instalador (id, nombre_id, cuadrilla_id, observacion) FROM stdin;
\.


--
-- TOC entry 2696 (class 0 OID 0)
-- Dependencies: 210
-- Name: ingresos_instalador_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ingresos_instalador_id_seq', 1, false);


--
-- TOC entry 2576 (class 0 OID 27654)
-- Dependencies: 211
-- Data for Name: ingresos_materialdeactividad; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_materialdeactividad (id, material_id, actividad_id, cantidad, observacion) FROM stdin;
\.


--
-- TOC entry 2697 (class 0 OID 0)
-- Dependencies: 212
-- Name: ingresos_materialdeactividad_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ingresos_materialdeactividad_id_seq', 1, false);


--
-- TOC entry 2578 (class 0 OID 27659)
-- Dependencies: 213
-- Data for Name: ingresos_modelodemedidor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_modelodemedidor (id, descripcion) FROM stdin;
ESP-65	ELECTRÓNICO 1F2C ACTIVA Y DEMANDA
ESP-70	ELECTRONICO 1F2C, A1R-L 3S CL 20
ESP-90	ELECTRONICO 1F3C, A1R 4S, CL 20
ESP-80	ELECTRONICO 1F3C, A1R 2S CL 200
ESP-100	ELECTRONICO 1F3C, A1R, 4SPLUS, CL 20
ESP-105	BIFASICO ELECTRÓ. ACT, REAC Y DEMAN
ESP-110	ELECTRONICO 3F3C, A1R-AL, 5S CL20
ESP-120	ELECTRONICO 3F3C, A1R-AL, 5S PLUS,CL 20
ESP-130	ELECTRONICO 3F4C, ACTIVA Y REACTIVA
ESP-140	ELECTRONICO 3F4C,ACT. REAC. Y DEMANDA
ESP-150	ELECTRONICO 3F4C, A1D, 16A, CL 100
ESP-160	ELECTRONICO 3F4C, A1R, 16A, CL 100
ESP-170	ELECTRONICO 3F4C, A1R-LQ,16APLUS, CL 100
ESP-180	ELECTRONICO 3F4C, A1R, 16S, CL 200
ESP-190	ELECTRONICO 3F4C,A1R-LQ, 16S, PLUS,CL200
ESP-200	ELECTRONICO 3F4C,A1R-LQ, 10A, CL20
ESP-210	ELECTRONICO 3F4C,A1R-LQ,10A, PLUS,CL20
ESP-220	ELECTRONICO 3F4C,A1R, 9S, CL 20
ESP-230	ELECTRONICO 3F4C, A1R-AL, 9S, CL 20
ESP-240	ELECTRONICO 3F4C, A1R-AL, 5A, CL 20
NOR-10	MONOFASICO DOS CONDUCTORES
NOR-20	MONOFASICO TRES CONDUCTORES
NOR-25	BIFASICO TRES CONDUCTORES
NOR-30	TRIFASICO CUATRO CONDUCTORES
NOR-40	TRIFASICO 3F4C, CON REACTIVA
NOR-50	TRIFASICO 3F4C, CON REACTIVA INDIRECTO
NOR-60	TRIFASICO 3F4C,REACT. Y REG. DEMANDA
\.


--
-- TOC entry 2579 (class 0 OID 27662)
-- Dependencies: 214
-- Data for Name: ingresos_motivoparasolicitud; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_motivoparasolicitud (id, descripcion) FROM stdin;
2	PLAN REP - PERDIDAS
1	SOLICITADO CLIENTE
20	SOLIC. CONTROL PERDI.
\.


--
-- TOC entry 2580 (class 0 OID 27666)
-- Dependencies: 215
-- Data for Name: ingresos_nivelsocieconomico; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_nivelsocieconomico (id, descripcion) FROM stdin;
\.


--
-- TOC entry 2581 (class 0 OID 27669)
-- Dependencies: 216
-- Data for Name: ingresos_parroquia; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_parroquia (id, num, descripcion, canton_id) FROM stdin;
1	50	CABECERA CANTONAL	5
2	55	LAS PALMAS	5
3	56	PUCARA	5
4	52	SAN RAFAEL DE SHARUG	5
5	53	SANTA CECILIA 2 	5
6	51	SARAYUNGA	5
7	54	TRES BANDERAS	5
8	50	PONCE ENRIQUEZ	6
9	1	MOLLETURO	7
10	1	SANTA ISABEL	8
11	51	*EL CAMBIO	2
12	5	EL CAMBIO	2
13	52	EL RETIRO	2
14	6	JAMBELI.	2
15	12	JUBONES	2
16	1	LA PROVIDENCIA	2
17	2	MACHALA	2
18	50	MACHALA, CABECERA CA	2
19	4	NUEVE DE MAYO	2
20	3	PUERTO BOLIVAR	2
21	52	*LA LIBERTAD	9
22	53	*LAS LAJAS (CAB. EN	9
23	50	ARENILLAS, CABECERA	9
24	55	CARCABON	9
25	51	CHACRAS	9
26	54	PALMARES	9
27	51	AYAPAMBA	10
28	56	CERRO AZUL	10
29	52	CORDONCILLO	10
30	53	MILAGRO	10
31	50	PACCHA, CABECERA CAN	10
32	54	SAN JOSE	10
33	55	SAN JOSE DE CERRO AZ	10
34	50	BALSAS, CABECERA CAN	11
35	51	BELLAMARIA	11
36	50	CHILLA, CABECERA CAN	12
37	51	SAN RAFAEL	12
38	52	DUMARI	12
39	51	BARBONES (SUCRE)	13
40	50	EL GUABO, CABECERA C	13
41	52	LA IBERIA	13
42	54	RIO BONITO	13
43	53	TENDALES (CAB.EN PUE	13
44	53	CARCA 1	14
45	8	CHACRAS1	14
46	1	ECUADOR	14
47	2	EL PARAISO	14
48	3	HUALTACO	14
49	50	HUAQUILLAS, CABECERA	14
50	54	JAMBELI	14
51	55	JAMBELI NO	14
52	4	MILTON REYES	14
53	5	UNION LOJANA	14
54	6	ZONA RURAL ARENILLAS	14
55	51	EL INGENIO	15
56	50	MARCABELI, CABECERA	15
57	1	BOLIBAR	16
58	51	BUENAVISTA	16
59	56	CAÑAQUEMADA	16
60	52	CASACAY	16
61	58	CERRO AZUL	16
62	53	LA PEAÑA	16
63	2	LOMA DE FRANCO	16
64	3	OCHOA LEON (MATRIZ)	16
65	50	PASAJE, CABECERA CAN	16
66	54	PROGRESO	16
67	57	SANTA CECILIA	16
68	4	TRES CERRITOS	16
69	55	UZHCURRUMI	16
70	51	CAPIRO (CAB. EN LA C	17
71	52	LA BOCANA	17
72	1	LA MATRIZ	17
73	2	LA SUSAYA	17
74	53	MOROMORO (CAB. EN EL	17
75	3	PIÑAS GRANDE	17
76	50	PIÑAS, CABECERA CANT	17
77	57	PIEDRA BLANCA	17
78	54	PIEDRAS	17
79	55	SAN ROQUE (AMBROSIO	17
80	56	SARACAY	17
81	51	CURTINCAPA	18
82	52	MORALES	18
83	50	PORTOVELO, CABECERA	18
84	53	SALATI	18
85	57	BELLAMARIA	3
86	51	BELLAVISTA	3
87	52	JAMBELI	3
88	3	JAMBELI (SATELITE)	3
89	4	JUMON (SATELITE)	3
90	53	LA AVANZADA	3
91	5	NUEVO SANTA ROSA	3
92	2	PUERTO JELI	3
93	54	SAN ANTONIO	3
94	1	SANTA ROSA	3
95	50	SANTA ROSA, CABECERA	3
96	55	TORATA	3
97	56	VICTORIA	3
98	51	ABAÑIN	19
99	52	ARCAPAMBA	19
100	53	GUANAZAN	19
101	54	GUISHAGUIÑA	19
102	55	HUERTAS	19
103	56	MALVAS	19
104	57	MULUNCAY	19
105	59	SALVIAS	19
106	58	SINSAO	19
107	50	ZARUMA CABECERA	19
108	52	EL PARAISO	20
109	54	EL PROGRESO	20
110	51	LA LIBERTAD	20
111	1	LA VICTORIA	20
112	50	LA VICTORIA, CABECER	20
113	2	PLATANILLOS	20
114	53	SAN ISIDRO	20
115	3	VALLE HERMOSO	20
116	58	TENGUEL	21
117	50	BALAO, CABECERA CANT	25
118	20	PARROQUIA TENGUEL	23
119	50	NARANJAL,CABECERA CA	24
\.


--
-- TOC entry 2698 (class 0 OID 0)
-- Dependencies: 217
-- Name: ingresos_parroquia_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ingresos_parroquia_id_seq', 119, true);


--
-- TOC entry 2583 (class 0 OID 27675)
-- Dependencies: 218
-- Data for Name: ingresos_provincia; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_provincia (id, descripcion) FROM stdin;
7	EL ORO
9	GUAYAS
1	AZUAY
\.


--
-- TOC entry 2584 (class 0 OID 27679)
-- Dependencies: 219
-- Data for Name: ingresos_ruta; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_ruta (id, num, descripcion, sector_id) FROM stdin;
\.


--
-- TOC entry 2699 (class 0 OID 0)
-- Dependencies: 220
-- Name: ingresos_ruta_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ingresos_ruta_id_seq', 1, false);


--
-- TOC entry 2586 (class 0 OID 27685)
-- Dependencies: 221
-- Data for Name: ingresos_sector; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_sector (id, num, descripcion, canton_id) FROM stdin;
\.


--
-- TOC entry 2700 (class 0 OID 0)
-- Dependencies: 222
-- Name: ingresos_sector_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ingresos_sector_id_seq', 1, false);


--
-- TOC entry 2588 (class 0 OID 27691)
-- Dependencies: 223
-- Data for Name: ingresos_secuencia; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_secuencia (id, num, descripcion, ruta_id) FROM stdin;
\.


--
-- TOC entry 2701 (class 0 OID 0)
-- Dependencies: 224
-- Name: ingresos_secuencia_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ingresos_secuencia_id_seq', 1, false);


--
-- TOC entry 2590 (class 0 OID 27697)
-- Dependencies: 225
-- Data for Name: ingresos_tipocalle; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_tipocalle (descripcion, id) FROM stdin;
AVENIDA	AV
CALLE	CA
\.


--
-- TOC entry 2591 (class 0 OID 27700)
-- Dependencies: 226
-- Data for Name: ingresos_tipodeacometidared; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_tipodeacometidared (id, descripcion) FROM stdin;
AD	ADOSADA
AE	AEREA
AH	ANTIHURTO
SU	SUBTERRANEA
\.


--
-- TOC entry 2592 (class 0 OID 27703)
-- Dependencies: 227
-- Data for Name: ingresos_tipodeconstruccion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_tipodeconstruccion (id, descripcion) FROM stdin;
1	ADOBE
2	BAHARENQUE
3	BLOQUE
13	CAÑA
4	CONCRETO
6	KIOSKO DE MADERA
5	KIOSKO METALICO
7	LADRILLO
14	LOTE VACIO
9	MADERA
8	MIXTA
12	NAVE INDUSTRIAL
10	PANEL LUMINOSO
11	RELOJ DIGITAL
\.


--
-- TOC entry 2593 (class 0 OID 27707)
-- Dependencies: 228
-- Data for Name: ingresos_tipodeservicio; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_tipodeservicio (id, tension, descripcion) FROM stdin;
12M	MEDIA TENSION	MONOF. DOS HILOS
13M	MEDIA TENSION	MONOF. 3 HILOS
12B	BAJA TENSION	MONOFASICO 2 HILOS
13B	BAJA TENSION	MONOFASICO 3 HILOS
34A	ALTA TENSION	TRIFASICO ALTA T.
34B	BAJA TENSION	TRIFASICO BAJA T.
34M	MEDIA TENSION	TRIFASICO MEDIA T.
\.


--
-- TOC entry 2594 (class 0 OID 27710)
-- Dependencies: 229
-- Data for Name: ingresos_tipodesolicitud; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_tipodesolicitud (id, descripcion) FROM stdin;
1	SERVICIO NUEVO
11	CAMBIO DE MATERIALES
13	CAMBIO DE MEDIDOR
\.


--
-- TOC entry 2595 (class 0 OID 27714)
-- Dependencies: 230
-- Data for Name: ingresos_ubicacion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_ubicacion (id, parroquia_id, calle_id, interseccion_id, urbanizacion_id, caserio_id) FROM stdin;
\.


--
-- TOC entry 2702 (class 0 OID 0)
-- Dependencies: 231
-- Name: ingresos_ubicacion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ingresos_ubicacion_id_seq', 3, true);


--
-- TOC entry 2597 (class 0 OID 27719)
-- Dependencies: 232
-- Data for Name: ingresos_ubicaciondelmedidor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_ubicaciondelmedidor (id, descripcion) FROM stdin;
4	CERRAMIENTO
8	CONST. O CASA GUARDIA
10	CONST. O CASA GUARDIA
5	EN LA CAÑA
1	PARED FRONTAL
3	PARED LATERAL DER.
2	PARED LATERAL IZQ.
12	POSTE
6	TABLERO METALICO
7	ZAGUAN O PORTAL
\.


--
-- TOC entry 2598 (class 0 OID 27723)
-- Dependencies: 233
-- Data for Name: ingresos_urbanizacion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_urbanizacion (id, descripcion) FROM stdin;
\.


--
-- TOC entry 2703 (class 0 OID 0)
-- Dependencies: 234
-- Name: ingresos_urbanizacion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ingresos_urbanizacion_id_seq', 1, false);


--
-- TOC entry 2600 (class 0 OID 27728)
-- Dependencies: 235
-- Data for Name: ingresos_usodeenergia; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_usodeenergia (id, descripcion) FROM stdin;
RD	RESIDENCIAL
AS	ASISTENCIA SOCIAL BAJA TENSION
AB	ASISTENCIA SOCIAL BT CON DEMANDA
A3	ASISTENCIA SOCIAL BT CON DEMANDA HORARIA
AD	ASISTENCIA SOCIAL MEDIA TENSION
AH	ASISTENCIA SOCIAL MT CON DEMANDA HORARIA
T3	ASISTENCIA SOCIAL TERCERA EDAD BT DEMANDA HORARIA
AU	AUTOCONSUMO BAJA TERNSION
GD	AUTOCONSUMO CON DEMANDA HORARIA
DH	AUTOCONSUMO DEMANDA HORARIA
DD	AUTOCONSUMO MT CON DEMANDA
AM	AUTOCONSUMO PARA LOCALES EMPRESA MT
BP	BENEFICIO PUBLICO BAJA TENSION
BB	BENEFICIO PUBLICO BT CON DEMANDA
B3	BENEFICIO PUBLICO BT CON DEMANDA HORARIA
BH	BENEFICIO PUBLICO CON DEMANDA HORARIA
BD	BENEFICIO PUBLICO MEDIA TENSION
BJ	BOMBEO AGUA JUNTAS ADMINISTRADORAS AGUA POTABLE
BA	BOMBEO DE AGUA
WA	BOMBEO DE AGUA AGRICOLA Y PSICOLA CON DEMANDA
FH	BOMBEO DE AGUA AGRICOLA Y PSICOLA HORARIO
W3	BOMBEO DE AGUA BT CON DEMANDA HORARIA
WD	BOMBEO DE AGUA CON DEMANDA
WH	BOMBEO DE AGUA CON DEMANDA HORARIA
DA	CAPACIDADES ESPECIALES - ENTIDADES AS. SOCIAL B.T.
DB	CAPACIDADES ESPECIALES - ENTIDADES DMA B.T.
DR	CAPACIDADES ESPECIALES - ENTIDADES HORARIOS
DN	CAPACIDAES ESPECIALES M.T. CON DEMANDA
XH	CLIENTES SERVIDOS EN ALTA TENSION
CO	COMERCIAL BAJA TENSION
CB	COMERCIAL BAJA TENSION CON DEMANDA
C3	COMERCIAL BT CON DEMANDA HORARIA
CH	COMERCIAL CON DEMANDA HORARIA
CD	COMERCIAL MEDIA TENSION
CR	CULTO RELIGIOSO BAJA TENSION
U3	CULTO RELIGIOSO BT CON DEMANDA
UH	CULTO RELIGIOSO CON DEMANDA HORARIA
CK	CULTO RELIGIOSO MEDIA TENSION
MB	ENTIDAD MUNICIPAL BT CON DEMANDA
OB	ENTIDAD OFICIAL BT CON DEMANDA
MU	ENTIDADES MUNICIPALES BAJA TENSION
M3	ENTIDADES MUNICIPALES BT CON DEMANDA HORARIA
MH	ENTIDADES MUNICIPALES CON DEMANDA HORARIA
MD	ENTIDADES MUNICIPALES MEDIA TENSION
OF	ENTIDADES OFICIALES BAJA TENSION
O3	ENTIDADES OFICIALES BT CON DEMANDA HORARIA
OH	ENTIDADES OFICIALES CON DEMANDA HORARIA
OD	ENTIDADES OFICIALES MEDIA TENSION
ES	ESCENARIO DEPORTIVO BAJA TENSION
E3	ESCENARIO DEPORTIVO BT CON DEMANDA HORARIA
EH	ESCENARIO DEPORTIVO CON DEMANDA HORARIA
ED	ESCENARIO DEPORTIVO MEDIA TENSION
IP	ILUMINACION PUBLICA BAJO MEDICION
IA	INDUSTRIAL ARTESANAL
IB	INDUSTRIAL BAJA TENSION CON DEMANDA
I3	INDUSTRIAL BT CON MEDICION HORARIA
IH	INDUSTRIAL CON MEDICION HORARIA
KH	INDUSTRIAL CON MEDICION HORARIA CON INCENDIOS AT
JH	INDUSTRIAL CON MEDICION HORARIA CON INCENDIOS MT
ID	INDUSTRIAL MEDIA TENSION
LH	LOCAL DEPORTIVO CON DEMANDA HORARIA
SH	PREVIO IND CON MEDICION HORARIA CON INCENTIVOS AT
RC	RESIDENCIAL COMUNITARIO
RT	RESIDENCIAL O DOMESTICO TEMPORAL
DS	RESIDENCIAL-CAPACIDAD ESPECIAL B.T.
DM	RESIDENCIAL-CAPACIDAD ESPECIAL M.T.
SC	SERVICIO COMUNITARIO BAJA TENSION
SD	SERVICIO COMUNITARIO MEDIA TENSION
TB	TERCERA EDAD ENTIDADES BT DEMANDA
VR	VENTA PARA REVENTA
\.


--
-- TOC entry 2601 (class 0 OID 27731)
-- Dependencies: 236
-- Data for Name: ingresos_usoespecificodelinmueble; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_usoespecificodelinmueble (id, "usoGeneral_id", descripcion) FROM stdin;
3	12	TIENDA-VIVIENDA
4	12	ZAPATERIA-VIVIENDA
2	12	PEQUEÑO NEGOCIO
1	12	 
\.


--
-- TOC entry 2602 (class 0 OID 27735)
-- Dependencies: 237
-- Data for Name: ingresos_usogeneraldelinmueble; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ingresos_usogeneraldelinmueble (id, descripcion) FROM stdin;
1	ALUMBRADO PUBLICO
2	ASISTENCIA SOCIAL
3	AUTOCONSUMO
4	BENEFICIO PUBLICO
5	BOMBEO DE AGUA
6	COMERCIAL
7	CULTO RELIGIOSO
8	ENTIDAD MUNICIPAL
9	ENTIDAD OFICIAL
13	ESCENARIO DEPORTIVO
10	INDUSTRIAL
11	LOCAL DEPORTIVO
12	RESIDENCIAL
\.


--
-- TOC entry 2603 (class 0 OID 27739)
-- Dependencies: 238
-- Data for Name: inventario_contrato; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY inventario_contrato (num, descripcion, zonas, "codigoInstalador", "inicioVigencia", "finalVigencia") FROM stdin;
0000008-14	perdidas 14 - Machala	Machala	130	2014-11-01	2015-06-20
\.


--
-- TOC entry 2604 (class 0 OID 27743)
-- Dependencies: 239
-- Data for Name: inventario_detallematerialcontrato; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY inventario_detallematerialcontrato (id, material_id, contrato_id, stock, unidad, proporcionado) FROM stdin;
\.


--
-- TOC entry 2704 (class 0 OID 0)
-- Dependencies: 240
-- Name: inventario_detallematerialcontrato_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('inventario_detallematerialcontrato_id_seq', 1, false);


--
-- TOC entry 2606 (class 0 OID 27748)
-- Dependencies: 241
-- Data for Name: inventario_detallerubro; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY inventario_detallerubro (id, contrato_id, servicio_id, rubro_id, "precioUnitario") FROM stdin;
\.


--
-- TOC entry 2705 (class 0 OID 0)
-- Dependencies: 242
-- Name: inventario_detallerubro_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('inventario_detallerubro_id_seq', 1, false);


--
-- TOC entry 2608 (class 0 OID 27753)
-- Dependencies: 243
-- Data for Name: inventario_marca; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY inventario_marca (id, descripcion) FROM stdin;
\.


--
-- TOC entry 2609 (class 0 OID 27756)
-- Dependencies: 244
-- Data for Name: inventario_material; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY inventario_material (id, descripcion, "voltajeSoportado") FROM stdin;
\.


--
-- TOC entry 2706 (class 0 OID 0)
-- Dependencies: 245
-- Name: inventario_material_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('inventario_material_id_seq', 1, false);


--
-- TOC entry 2611 (class 0 OID 27762)
-- Dependencies: 246
-- Data for Name: inventario_medidor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY inventario_medidor (id, contrato_id, fabrica, serie, marca_id, tipo, digitos, hilos, fases, voltaje, est, modelo_id) FROM stdin;
\.


--
-- TOC entry 2707 (class 0 OID 0)
-- Dependencies: 247
-- Name: inventario_medidor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('inventario_medidor_id_seq', 1, false);


--
-- TOC entry 2613 (class 0 OID 27771)
-- Dependencies: 248
-- Data for Name: inventario_rangodematerial; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY inventario_rangodematerial (id, "detalleMaterialContrato_id", inicio, final) FROM stdin;
\.


--
-- TOC entry 2708 (class 0 OID 0)
-- Dependencies: 249
-- Name: inventario_rangodematerial_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('inventario_rangodematerial_id_seq', 1, false);


--
-- TOC entry 2615 (class 0 OID 27776)
-- Dependencies: 250
-- Data for Name: inventario_rubro; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY inventario_rubro (id, descripcion) FROM stdin;
\.


--
-- TOC entry 2709 (class 0 OID 0)
-- Dependencies: 251
-- Name: inventario_rubro_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('inventario_rubro_id_seq', 1, false);


--
-- TOC entry 2617 (class 0 OID 27781)
-- Dependencies: 252
-- Data for Name: inventario_sello; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY inventario_sello (id, "detalleMaterialContrato_id", numero, color, ubicacion, estado) FROM stdin;
\.


--
-- TOC entry 2710 (class 0 OID 0)
-- Dependencies: 253
-- Name: inventario_sello_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('inventario_sello_id_seq', 1, false);


--
-- TOC entry 2619 (class 0 OID 27787)
-- Dependencies: 254
-- Data for Name: inventario_servicio; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY inventario_servicio (id, descripcion) FROM stdin;
\.


--
-- TOC entry 2711 (class 0 OID 0)
-- Dependencies: 255
-- Name: inventario_servicio_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('inventario_servicio_id_seq', 1, false);


--
-- TOC entry 2621 (class 0 OID 27792)
-- Dependencies: 256
-- Data for Name: inventario_subtipodematerial; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY inventario_subtipodematerial (id, "tipoDeMaterial_id", descripcion) FROM stdin;
\.


--
-- TOC entry 2712 (class 0 OID 0)
-- Dependencies: 257
-- Name: inventario_subtipodematerial_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('inventario_subtipodematerial_id_seq', 1, false);


--
-- TOC entry 2623 (class 0 OID 27797)
-- Dependencies: 258
-- Data for Name: inventario_tipodematerial; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY inventario_tipodematerial (id, material_id, descripcion) FROM stdin;
\.


--
-- TOC entry 2713 (class 0 OID 0)
-- Dependencies: 259
-- Name: inventario_tipodematerial_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('inventario_tipodematerial_id_seq', 1, false);


--
-- TOC entry 2625 (class 0 OID 27802)
-- Dependencies: 260
-- Data for Name: usuarios_usuariosico; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY usuarios_usuariosico (id, nombre, clave, contrato_id) FROM stdin;
1	lzambrano	lzambrano	0000008-14
\.


--
-- TOC entry 2714 (class 0 OID 0)
-- Dependencies: 261
-- Name: usuarios_usuariosico_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('usuarios_usuariosico_id_seq', 1, true);


--
-- TOC entry 2133 (class 2606 OID 27848)
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- TOC entry 2139 (class 2606 OID 27850)
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- TOC entry 2142 (class 2606 OID 27852)
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 2136 (class 2606 OID 27854)
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- TOC entry 2145 (class 2606 OID 27856)
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- TOC entry 2147 (class 2606 OID 27858)
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- TOC entry 2155 (class 2606 OID 27860)
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- TOC entry 2158 (class 2606 OID 27862)
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- TOC entry 2149 (class 2606 OID 27864)
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- TOC entry 2161 (class 2606 OID 27866)
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 2164 (class 2606 OID 27868)
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- TOC entry 2151 (class 2606 OID 27870)
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- TOC entry 2166 (class 2606 OID 27872)
-- Name: auth_user_usuario_sico_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_usuario_sico
    ADD CONSTRAINT auth_user_usuario_sico_pkey PRIMARY KEY (id);


--
-- TOC entry 2169 (class 2606 OID 27874)
-- Name: auth_user_usuario_sico_user_id_usuariosico_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_usuario_sico
    ADD CONSTRAINT auth_user_usuario_sico_user_id_usuariosico_id_key UNIQUE (user_id, usuariosico_id);


--
-- TOC entry 2172 (class 2606 OID 27876)
-- Name: busquedas_vitacorabusquedas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY busquedas_vitacorabusquedas
    ADD CONSTRAINT busquedas_vitacorabusquedas_pkey PRIMARY KEY (id);


--
-- TOC entry 2176 (class 2606 OID 27878)
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- TOC entry 2179 (class 2606 OID 27880)
-- Name: django_content_type_app_label_model_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_key UNIQUE (app_label, model);


--
-- TOC entry 2181 (class 2606 OID 27882)
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- TOC entry 2184 (class 2606 OID 27884)
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- TOC entry 2198 (class 2606 OID 27886)
-- Name: ingresos_actividad_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_actividad
    ADD CONSTRAINT ingresos_actividad_pkey PRIMARY KEY (id);


--
-- TOC entry 2208 (class 2606 OID 27888)
-- Name: ingresos_calibredelared_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_calibredelared
    ADD CONSTRAINT ingresos_calibredelared_pkey PRIMARY KEY (id);


--
-- TOC entry 2210 (class 2606 OID 27890)
-- Name: ingresos_calle_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_calle
    ADD CONSTRAINT ingresos_calle_pkey PRIMARY KEY (id);


--
-- TOC entry 2212 (class 2606 OID 27892)
-- Name: ingresos_canton_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_canton
    ADD CONSTRAINT ingresos_canton_pkey PRIMARY KEY (id);


--
-- TOC entry 2215 (class 2606 OID 27894)
-- Name: ingresos_caserio_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_caserio
    ADD CONSTRAINT ingresos_caserio_pkey PRIMARY KEY (id);


--
-- TOC entry 2218 (class 2606 OID 27896)
-- Name: ingresos_clasered_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_clasered
    ADD CONSTRAINT ingresos_clasered_pkey PRIMARY KEY (id);


--
-- TOC entry 2220 (class 2606 OID 27898)
-- Name: ingresos_cliente_geocodigo_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_cliente
    ADD CONSTRAINT ingresos_cliente_geocodigo_id_key UNIQUE (geocodigo_id);


--
-- TOC entry 2222 (class 2606 OID 27900)
-- Name: ingresos_cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_cliente
    ADD CONSTRAINT ingresos_cliente_pkey PRIMARY KEY (id);


--
-- TOC entry 2224 (class 2606 OID 27902)
-- Name: ingresos_cliente_ubicacionGeografica_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_cliente
    ADD CONSTRAINT "ingresos_cliente_ubicacionGeografica_id_key" UNIQUE ("ubicacionGeografica_id");


--
-- TOC entry 2226 (class 2606 OID 27904)
-- Name: ingresos_cuadrilla_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_cuadrilla
    ADD CONSTRAINT ingresos_cuadrilla_pkey PRIMARY KEY (id);


--
-- TOC entry 2228 (class 2606 OID 27906)
-- Name: ingresos_demanda_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_demanda
    ADD CONSTRAINT ingresos_demanda_pkey PRIMARY KEY (id);


--
-- TOC entry 2232 (class 2606 OID 27908)
-- Name: ingresos_detalleclientemedidor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_detalleclientemedidor
    ADD CONSTRAINT ingresos_detalleclientemedidor_pkey PRIMARY KEY (id);


--
-- TOC entry 2235 (class 2606 OID 27910)
-- Name: ingresos_detalleclientereferencia_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_detalleclientereferencia
    ADD CONSTRAINT ingresos_detalleclientereferencia_pkey PRIMARY KEY (id);


--
-- TOC entry 2240 (class 2606 OID 27912)
-- Name: ingresos_detalledeactividad_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_detalledeactividad
    ADD CONSTRAINT ingresos_detalledeactividad_pkey PRIMARY KEY (id);


--
-- TOC entry 2243 (class 2606 OID 27914)
-- Name: ingresos_empleado_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_empleado
    ADD CONSTRAINT ingresos_empleado_pkey PRIMARY KEY (id);


--
-- TOC entry 2245 (class 2606 OID 27916)
-- Name: ingresos_estadodeunainstalacion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_estadodeunainstalacion
    ADD CONSTRAINT ingresos_estadodeunainstalacion_pkey PRIMARY KEY (id);


--
-- TOC entry 2247 (class 2606 OID 27918)
-- Name: ingresos_formadeconexion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_formadeconexion
    ADD CONSTRAINT ingresos_formadeconexion_pkey PRIMARY KEY (id);


--
-- TOC entry 2250 (class 2606 OID 27920)
-- Name: ingresos_foto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_foto
    ADD CONSTRAINT ingresos_foto_pkey PRIMARY KEY (id);


--
-- TOC entry 2254 (class 2606 OID 27922)
-- Name: ingresos_instalador_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_instalador
    ADD CONSTRAINT ingresos_instalador_pkey PRIMARY KEY (id);


--
-- TOC entry 2258 (class 2606 OID 27924)
-- Name: ingresos_materialdeactividad_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_materialdeactividad
    ADD CONSTRAINT ingresos_materialdeactividad_pkey PRIMARY KEY (id);


--
-- TOC entry 2261 (class 2606 OID 27926)
-- Name: ingresos_modelodemedidor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_modelodemedidor
    ADD CONSTRAINT ingresos_modelodemedidor_pkey PRIMARY KEY (id);


--
-- TOC entry 2263 (class 2606 OID 27928)
-- Name: ingresos_motivoparasolicitud_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_motivoparasolicitud
    ADD CONSTRAINT ingresos_motivoparasolicitud_pkey PRIMARY KEY (id);


--
-- TOC entry 2266 (class 2606 OID 27930)
-- Name: ingresos_nivelsocieconomico_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_nivelsocieconomico
    ADD CONSTRAINT ingresos_nivelsocieconomico_pkey PRIMARY KEY (id);


--
-- TOC entry 2269 (class 2606 OID 27932)
-- Name: ingresos_parroquia_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_parroquia
    ADD CONSTRAINT ingresos_parroquia_pkey PRIMARY KEY (id);


--
-- TOC entry 2271 (class 2606 OID 27934)
-- Name: ingresos_provincia_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_provincia
    ADD CONSTRAINT ingresos_provincia_pkey PRIMARY KEY (id);


--
-- TOC entry 2273 (class 2606 OID 27936)
-- Name: ingresos_ruta_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_ruta
    ADD CONSTRAINT ingresos_ruta_pkey PRIMARY KEY (id);


--
-- TOC entry 2277 (class 2606 OID 27938)
-- Name: ingresos_sector_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_sector
    ADD CONSTRAINT ingresos_sector_pkey PRIMARY KEY (id);


--
-- TOC entry 2279 (class 2606 OID 27940)
-- Name: ingresos_secuencia_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_secuencia
    ADD CONSTRAINT ingresos_secuencia_pkey PRIMARY KEY (id);


--
-- TOC entry 2282 (class 2606 OID 27942)
-- Name: ingresos_tipocalle_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_tipocalle
    ADD CONSTRAINT ingresos_tipocalle_pkey PRIMARY KEY (id);


--
-- TOC entry 2285 (class 2606 OID 27944)
-- Name: ingresos_tipodeacometidared_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_tipodeacometidared
    ADD CONSTRAINT ingresos_tipodeacometidared_pkey PRIMARY KEY (id);


--
-- TOC entry 2287 (class 2606 OID 27946)
-- Name: ingresos_tipodeconstruccion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_tipodeconstruccion
    ADD CONSTRAINT ingresos_tipodeconstruccion_pkey PRIMARY KEY (id);


--
-- TOC entry 2290 (class 2606 OID 27948)
-- Name: ingresos_tipodeservicio_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_tipodeservicio
    ADD CONSTRAINT ingresos_tipodeservicio_pkey PRIMARY KEY (id);


--
-- TOC entry 2292 (class 2606 OID 27950)
-- Name: ingresos_tipodesolicitud_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_tipodesolicitud
    ADD CONSTRAINT ingresos_tipodesolicitud_pkey PRIMARY KEY (id);


--
-- TOC entry 2298 (class 2606 OID 27952)
-- Name: ingresos_ubicacion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_ubicacion
    ADD CONSTRAINT ingresos_ubicacion_pkey PRIMARY KEY (id);


--
-- TOC entry 2301 (class 2606 OID 27954)
-- Name: ingresos_ubicaciondelmedidor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_ubicaciondelmedidor
    ADD CONSTRAINT ingresos_ubicaciondelmedidor_pkey PRIMARY KEY (id);


--
-- TOC entry 2303 (class 2606 OID 27956)
-- Name: ingresos_urbanizacion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_urbanizacion
    ADD CONSTRAINT ingresos_urbanizacion_pkey PRIMARY KEY (id);


--
-- TOC entry 2306 (class 2606 OID 27958)
-- Name: ingresos_usodeenergia_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_usodeenergia
    ADD CONSTRAINT ingresos_usodeenergia_pkey PRIMARY KEY (id);


--
-- TOC entry 2308 (class 2606 OID 27960)
-- Name: ingresos_usoespecificodelinmueble_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_usoespecificodelinmueble
    ADD CONSTRAINT ingresos_usoespecificodelinmueble_pkey PRIMARY KEY (id);


--
-- TOC entry 2311 (class 2606 OID 27962)
-- Name: ingresos_usogeneraldelinmueble_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ingresos_usogeneraldelinmueble
    ADD CONSTRAINT ingresos_usogeneraldelinmueble_pkey PRIMARY KEY (id);


--
-- TOC entry 2314 (class 2606 OID 27964)
-- Name: inventario_contrato_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY inventario_contrato
    ADD CONSTRAINT inventario_contrato_pkey PRIMARY KEY (num);


--
-- TOC entry 2319 (class 2606 OID 27966)
-- Name: inventario_detallematerialcontrato_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY inventario_detallematerialcontrato
    ADD CONSTRAINT inventario_detallematerialcontrato_pkey PRIMARY KEY (id);


--
-- TOC entry 2323 (class 2606 OID 27968)
-- Name: inventario_detallerubro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY inventario_detallerubro
    ADD CONSTRAINT inventario_detallerubro_pkey PRIMARY KEY (id);


--
-- TOC entry 2328 (class 2606 OID 27970)
-- Name: inventario_marca_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY inventario_marca
    ADD CONSTRAINT inventario_marca_pkey PRIMARY KEY (id);


--
-- TOC entry 2330 (class 2606 OID 27972)
-- Name: inventario_material_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY inventario_material
    ADD CONSTRAINT inventario_material_pkey PRIMARY KEY (id);


--
-- TOC entry 2337 (class 2606 OID 27974)
-- Name: inventario_medidor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY inventario_medidor
    ADD CONSTRAINT inventario_medidor_pkey PRIMARY KEY (id);


--
-- TOC entry 2339 (class 2606 OID 27976)
-- Name: inventario_rangodematerial_detalleMaterialContrato_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY inventario_rangodematerial
    ADD CONSTRAINT "inventario_rangodematerial_detalleMaterialContrato_id_key" UNIQUE ("detalleMaterialContrato_id");


--
-- TOC entry 2341 (class 2606 OID 27978)
-- Name: inventario_rangodematerial_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY inventario_rangodematerial
    ADD CONSTRAINT inventario_rangodematerial_pkey PRIMARY KEY (id);


--
-- TOC entry 2343 (class 2606 OID 27980)
-- Name: inventario_rubro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY inventario_rubro
    ADD CONSTRAINT inventario_rubro_pkey PRIMARY KEY (id);


--
-- TOC entry 2346 (class 2606 OID 27982)
-- Name: inventario_sello_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY inventario_sello
    ADD CONSTRAINT inventario_sello_pkey PRIMARY KEY (id);


--
-- TOC entry 2348 (class 2606 OID 27984)
-- Name: inventario_servicio_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY inventario_servicio
    ADD CONSTRAINT inventario_servicio_pkey PRIMARY KEY (id);


--
-- TOC entry 2350 (class 2606 OID 27986)
-- Name: inventario_subtipodematerial_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY inventario_subtipodematerial
    ADD CONSTRAINT inventario_subtipodematerial_pkey PRIMARY KEY (id);


--
-- TOC entry 2354 (class 2606 OID 27988)
-- Name: inventario_tipodematerial_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY inventario_tipodematerial
    ADD CONSTRAINT inventario_tipodematerial_pkey PRIMARY KEY (id);


--
-- TOC entry 2358 (class 2606 OID 27990)
-- Name: usuarios_usuariosico_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY usuarios_usuariosico
    ADD CONSTRAINT usuarios_usuariosico_pkey PRIMARY KEY (id);


--
-- TOC entry 2134 (class 1259 OID 27991)
-- Name: auth_group_name_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_name_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- TOC entry 2137 (class 1259 OID 27992)
-- Name: auth_group_permissions_group_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_permissions_group_id ON auth_group_permissions USING btree (group_id);


--
-- TOC entry 2140 (class 1259 OID 27993)
-- Name: auth_group_permissions_permission_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_permissions_permission_id ON auth_group_permissions USING btree (permission_id);


--
-- TOC entry 2143 (class 1259 OID 27994)
-- Name: auth_permission_content_type_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_permission_content_type_id ON auth_permission USING btree (content_type_id);


--
-- TOC entry 2153 (class 1259 OID 27995)
-- Name: auth_user_groups_group_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_groups_group_id ON auth_user_groups USING btree (group_id);


--
-- TOC entry 2156 (class 1259 OID 27996)
-- Name: auth_user_groups_user_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_groups_user_id ON auth_user_groups USING btree (user_id);


--
-- TOC entry 2159 (class 1259 OID 27997)
-- Name: auth_user_user_permissions_permission_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_permission_id ON auth_user_user_permissions USING btree (permission_id);


--
-- TOC entry 2162 (class 1259 OID 27998)
-- Name: auth_user_user_permissions_user_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_user_id ON auth_user_user_permissions USING btree (user_id);


--
-- TOC entry 2152 (class 1259 OID 27999)
-- Name: auth_user_username_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_username_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- TOC entry 2167 (class 1259 OID 28000)
-- Name: auth_user_usuario_sico_user_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_usuario_sico_user_id ON auth_user_usuario_sico USING btree (user_id);


--
-- TOC entry 2170 (class 1259 OID 28001)
-- Name: auth_user_usuario_sico_usuariosico_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_usuario_sico_usuariosico_id ON auth_user_usuario_sico USING btree (usuariosico_id);


--
-- TOC entry 2173 (class 1259 OID 28002)
-- Name: busquedas_vitacorabusquedas_usuario_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX busquedas_vitacorabusquedas_usuario_id ON busquedas_vitacorabusquedas USING btree (usuario_id);


--
-- TOC entry 2174 (class 1259 OID 28003)
-- Name: django_admin_log_content_type_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_admin_log_content_type_id ON django_admin_log USING btree (content_type_id);


--
-- TOC entry 2177 (class 1259 OID 28004)
-- Name: django_admin_log_user_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_admin_log_user_id ON django_admin_log USING btree (user_id);


--
-- TOC entry 2182 (class 1259 OID 28005)
-- Name: django_session_expire_date; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_session_expire_date ON django_session USING btree (expire_date);


--
-- TOC entry 2185 (class 1259 OID 28006)
-- Name: django_session_session_key_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_session_session_key_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- TOC entry 2186 (class 1259 OID 28007)
-- Name: ingresos_actividad_calibreDeLaRed_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "ingresos_actividad_calibreDeLaRed_id" ON ingresos_actividad USING btree ("calibreDeLaRed_id");


--
-- TOC entry 2187 (class 1259 OID 28008)
-- Name: ingresos_actividad_claseRed_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "ingresos_actividad_claseRed_id" ON ingresos_actividad USING btree ("claseRed_id");


--
-- TOC entry 2188 (class 1259 OID 28009)
-- Name: ingresos_actividad_claseRed_id_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "ingresos_actividad_claseRed_id_like" ON ingresos_actividad USING btree ("claseRed_id" varchar_pattern_ops);


--
-- TOC entry 2189 (class 1259 OID 28010)
-- Name: ingresos_actividad_cliente_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_actividad_cliente_id ON ingresos_actividad USING btree (cliente_id);


--
-- TOC entry 2190 (class 1259 OID 28011)
-- Name: ingresos_actividad_demanda_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_actividad_demanda_id ON ingresos_actividad USING btree (demanda_id);


--
-- TOC entry 2191 (class 1259 OID 28012)
-- Name: ingresos_actividad_estadoDeLaInstalacion_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "ingresos_actividad_estadoDeLaInstalacion_id" ON ingresos_actividad USING btree ("estadoDeLaInstalacion_id");


--
-- TOC entry 2192 (class 1259 OID 28013)
-- Name: ingresos_actividad_formaDeConexion_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "ingresos_actividad_formaDeConexion_id" ON ingresos_actividad USING btree ("formaDeConexion_id");


--
-- TOC entry 2193 (class 1259 OID 28014)
-- Name: ingresos_actividad_instalador_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_actividad_instalador_id ON ingresos_actividad USING btree (instalador_id);


--
-- TOC entry 2194 (class 1259 OID 28015)
-- Name: ingresos_actividad_motivoDeSolicitud_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "ingresos_actividad_motivoDeSolicitud_id" ON ingresos_actividad USING btree ("motivoDeSolicitud_id");


--
-- TOC entry 2195 (class 1259 OID 28016)
-- Name: ingresos_actividad_nivelSocieconomico_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "ingresos_actividad_nivelSocieconomico_id" ON ingresos_actividad USING btree ("nivelSocieconomico_id");


--
-- TOC entry 2196 (class 1259 OID 28017)
-- Name: ingresos_actividad_nivelSocieconomico_id_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "ingresos_actividad_nivelSocieconomico_id_like" ON ingresos_actividad USING btree ("nivelSocieconomico_id" varchar_pattern_ops);


--
-- TOC entry 2199 (class 1259 OID 28018)
-- Name: ingresos_actividad_tipoDeAcometidaRed_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "ingresos_actividad_tipoDeAcometidaRed_id" ON ingresos_actividad USING btree ("tipoDeAcometidaRed_id");


--
-- TOC entry 2200 (class 1259 OID 28019)
-- Name: ingresos_actividad_tipoDeAcometidaRed_id_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "ingresos_actividad_tipoDeAcometidaRed_id_like" ON ingresos_actividad USING btree ("tipoDeAcometidaRed_id" varchar_pattern_ops);


--
-- TOC entry 2201 (class 1259 OID 28020)
-- Name: ingresos_actividad_tipoDeConstruccion_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "ingresos_actividad_tipoDeConstruccion_id" ON ingresos_actividad USING btree ("tipoDeConstruccion_id");


--
-- TOC entry 2202 (class 1259 OID 28021)
-- Name: ingresos_actividad_tipoDeSolicitud_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "ingresos_actividad_tipoDeSolicitud_id" ON ingresos_actividad USING btree ("tipoDeSolicitud_id");


--
-- TOC entry 2203 (class 1259 OID 28022)
-- Name: ingresos_actividad_ubicacionDelMedidor_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "ingresos_actividad_ubicacionDelMedidor_id" ON ingresos_actividad USING btree ("ubicacionDelMedidor_id");


--
-- TOC entry 2204 (class 1259 OID 28023)
-- Name: ingresos_actividad_usoDeEnergia_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "ingresos_actividad_usoDeEnergia_id" ON ingresos_actividad USING btree ("usoDeEnergia_id");


--
-- TOC entry 2205 (class 1259 OID 28024)
-- Name: ingresos_actividad_usoDeEnergia_id_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "ingresos_actividad_usoDeEnergia_id_like" ON ingresos_actividad USING btree ("usoDeEnergia_id" varchar_pattern_ops);


--
-- TOC entry 2206 (class 1259 OID 28025)
-- Name: ingresos_actividad_usoEspecificoDelInmueble_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "ingresos_actividad_usoEspecificoDelInmueble_id" ON ingresos_actividad USING btree ("usoEspecificoDelInmueble_id");


--
-- TOC entry 2213 (class 1259 OID 28026)
-- Name: ingresos_canton_provincia_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_canton_provincia_id ON ingresos_canton USING btree (provincia_id);


--
-- TOC entry 2216 (class 1259 OID 28027)
-- Name: ingresos_clasered_id_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_clasered_id_like ON ingresos_clasered USING btree (id varchar_pattern_ops);


--
-- TOC entry 2229 (class 1259 OID 28028)
-- Name: ingresos_detalleclientemedidor_cliente_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_detalleclientemedidor_cliente_id ON ingresos_detalleclientemedidor USING btree (cliente_id);


--
-- TOC entry 2230 (class 1259 OID 28029)
-- Name: ingresos_detalleclientemedidor_medidor_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_detalleclientemedidor_medidor_id ON ingresos_detalleclientemedidor USING btree (medidor_id);


--
-- TOC entry 2233 (class 1259 OID 28030)
-- Name: ingresos_detalleclientereferencia_cliente_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_detalleclientereferencia_cliente_id ON ingresos_detalleclientereferencia USING btree (cliente_id);


--
-- TOC entry 2236 (class 1259 OID 28031)
-- Name: ingresos_detalleclientereferencia_referencia_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_detalleclientereferencia_referencia_id ON ingresos_detalleclientereferencia USING btree (referencia_id);


--
-- TOC entry 2237 (class 1259 OID 28032)
-- Name: ingresos_detalleclientereferencia_ubicacion_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_detalleclientereferencia_ubicacion_id ON ingresos_detalleclientereferencia USING btree (ubicacion_id);


--
-- TOC entry 2238 (class 1259 OID 28033)
-- Name: ingresos_detalledeactividad_actividad_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_detalledeactividad_actividad_id ON ingresos_detalledeactividad USING btree (actividad_id);


--
-- TOC entry 2241 (class 1259 OID 28034)
-- Name: ingresos_detalledeactividad_rubro_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_detalledeactividad_rubro_id ON ingresos_detalledeactividad USING btree (rubro_id);


--
-- TOC entry 2248 (class 1259 OID 28035)
-- Name: ingresos_foto_actividad_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_foto_actividad_id ON ingresos_foto USING btree (actividad_id);


--
-- TOC entry 2251 (class 1259 OID 28036)
-- Name: ingresos_instalador_cuadrilla_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_instalador_cuadrilla_id ON ingresos_instalador USING btree (cuadrilla_id);


--
-- TOC entry 2252 (class 1259 OID 28037)
-- Name: ingresos_instalador_nombre_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_instalador_nombre_id ON ingresos_instalador USING btree (nombre_id);


--
-- TOC entry 2255 (class 1259 OID 28038)
-- Name: ingresos_materialdeactividad_actividad_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_materialdeactividad_actividad_id ON ingresos_materialdeactividad USING btree (actividad_id);


--
-- TOC entry 2256 (class 1259 OID 28039)
-- Name: ingresos_materialdeactividad_material_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_materialdeactividad_material_id ON ingresos_materialdeactividad USING btree (material_id);


--
-- TOC entry 2259 (class 1259 OID 28040)
-- Name: ingresos_modelodemedidor_id_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_modelodemedidor_id_like ON ingresos_modelodemedidor USING btree (id varchar_pattern_ops);


--
-- TOC entry 2264 (class 1259 OID 28041)
-- Name: ingresos_nivelsocieconomico_id_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_nivelsocieconomico_id_like ON ingresos_nivelsocieconomico USING btree (id varchar_pattern_ops);


--
-- TOC entry 2267 (class 1259 OID 28042)
-- Name: ingresos_parroquia_canton_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_parroquia_canton_id ON ingresos_parroquia USING btree (canton_id);


--
-- TOC entry 2274 (class 1259 OID 28043)
-- Name: ingresos_ruta_sector_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_ruta_sector_id ON ingresos_ruta USING btree (sector_id);


--
-- TOC entry 2275 (class 1259 OID 28044)
-- Name: ingresos_sector_canton_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_sector_canton_id ON ingresos_sector USING btree (canton_id);


--
-- TOC entry 2280 (class 1259 OID 28045)
-- Name: ingresos_secuencia_ruta_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_secuencia_ruta_id ON ingresos_secuencia USING btree (ruta_id);


--
-- TOC entry 2283 (class 1259 OID 28046)
-- Name: ingresos_tipodeacometidared_id_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_tipodeacometidared_id_like ON ingresos_tipodeacometidared USING btree (id varchar_pattern_ops);


--
-- TOC entry 2288 (class 1259 OID 28047)
-- Name: ingresos_tipodeservicio_id_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_tipodeservicio_id_like ON ingresos_tipodeservicio USING btree (id varchar_pattern_ops);


--
-- TOC entry 2293 (class 1259 OID 28048)
-- Name: ingresos_ubicacion_calle_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_ubicacion_calle_id ON ingresos_ubicacion USING btree (calle_id);


--
-- TOC entry 2294 (class 1259 OID 28049)
-- Name: ingresos_ubicacion_caserio_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_ubicacion_caserio_id ON ingresos_ubicacion USING btree (caserio_id);


--
-- TOC entry 2295 (class 1259 OID 28050)
-- Name: ingresos_ubicacion_interseccion_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_ubicacion_interseccion_id ON ingresos_ubicacion USING btree (interseccion_id);


--
-- TOC entry 2296 (class 1259 OID 28051)
-- Name: ingresos_ubicacion_parroquia_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_ubicacion_parroquia_id ON ingresos_ubicacion USING btree (parroquia_id);


--
-- TOC entry 2299 (class 1259 OID 28052)
-- Name: ingresos_ubicacion_urbanizacion_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_ubicacion_urbanizacion_id ON ingresos_ubicacion USING btree (urbanizacion_id);


--
-- TOC entry 2304 (class 1259 OID 28053)
-- Name: ingresos_usodeenergia_id_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX ingresos_usodeenergia_id_like ON ingresos_usodeenergia USING btree (id varchar_pattern_ops);


--
-- TOC entry 2309 (class 1259 OID 28054)
-- Name: ingresos_usoespecificodelinmueble_usoGeneral_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "ingresos_usoespecificodelinmueble_usoGeneral_id" ON ingresos_usoespecificodelinmueble USING btree ("usoGeneral_id");


--
-- TOC entry 2312 (class 1259 OID 28055)
-- Name: inventario_contrato_num_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX inventario_contrato_num_like ON inventario_contrato USING btree (num varchar_pattern_ops);


--
-- TOC entry 2315 (class 1259 OID 28056)
-- Name: inventario_detallematerialcontrato_contrato_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX inventario_detallematerialcontrato_contrato_id ON inventario_detallematerialcontrato USING btree (contrato_id);


--
-- TOC entry 2316 (class 1259 OID 28057)
-- Name: inventario_detallematerialcontrato_contrato_id_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX inventario_detallematerialcontrato_contrato_id_like ON inventario_detallematerialcontrato USING btree (contrato_id varchar_pattern_ops);


--
-- TOC entry 2317 (class 1259 OID 28058)
-- Name: inventario_detallematerialcontrato_material_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX inventario_detallematerialcontrato_material_id ON inventario_detallematerialcontrato USING btree (material_id);


--
-- TOC entry 2320 (class 1259 OID 28059)
-- Name: inventario_detallerubro_contrato_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX inventario_detallerubro_contrato_id ON inventario_detallerubro USING btree (contrato_id);


--
-- TOC entry 2321 (class 1259 OID 28060)
-- Name: inventario_detallerubro_contrato_id_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX inventario_detallerubro_contrato_id_like ON inventario_detallerubro USING btree (contrato_id varchar_pattern_ops);


--
-- TOC entry 2324 (class 1259 OID 28061)
-- Name: inventario_detallerubro_rubro_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX inventario_detallerubro_rubro_id ON inventario_detallerubro USING btree (rubro_id);


--
-- TOC entry 2325 (class 1259 OID 28062)
-- Name: inventario_detallerubro_servicio_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX inventario_detallerubro_servicio_id ON inventario_detallerubro USING btree (servicio_id);


--
-- TOC entry 2326 (class 1259 OID 28063)
-- Name: inventario_marca_id_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX inventario_marca_id_like ON inventario_marca USING btree (id varchar_pattern_ops);


--
-- TOC entry 2331 (class 1259 OID 28064)
-- Name: inventario_medidor_contrato_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX inventario_medidor_contrato_id ON inventario_medidor USING btree (contrato_id);


--
-- TOC entry 2332 (class 1259 OID 28065)
-- Name: inventario_medidor_marca_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX inventario_medidor_marca_id ON inventario_medidor USING btree (marca_id);


--
-- TOC entry 2333 (class 1259 OID 28066)
-- Name: inventario_medidor_marca_id_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX inventario_medidor_marca_id_like ON inventario_medidor USING btree (marca_id varchar_pattern_ops);


--
-- TOC entry 2334 (class 1259 OID 28067)
-- Name: inventario_medidor_modelo_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX inventario_medidor_modelo_id ON inventario_medidor USING btree (modelo_id);


--
-- TOC entry 2335 (class 1259 OID 28068)
-- Name: inventario_medidor_modelo_id_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX inventario_medidor_modelo_id_like ON inventario_medidor USING btree (modelo_id varchar_pattern_ops);


--
-- TOC entry 2344 (class 1259 OID 28069)
-- Name: inventario_sello_detalleMaterialContrato_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "inventario_sello_detalleMaterialContrato_id" ON inventario_sello USING btree ("detalleMaterialContrato_id");


--
-- TOC entry 2351 (class 1259 OID 28070)
-- Name: inventario_subtipodematerial_tipoDeMaterial_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "inventario_subtipodematerial_tipoDeMaterial_id" ON inventario_subtipodematerial USING btree ("tipoDeMaterial_id");


--
-- TOC entry 2352 (class 1259 OID 28071)
-- Name: inventario_tipodematerial_material_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX inventario_tipodematerial_material_id ON inventario_tipodematerial USING btree (material_id);


--
-- TOC entry 2355 (class 1259 OID 28072)
-- Name: usuarios_usuariosico_contrato_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX usuarios_usuariosico_contrato_id ON usuarios_usuariosico USING btree (contrato_id);


--
-- TOC entry 2356 (class 1259 OID 28073)
-- Name: usuarios_usuariosico_contrato_id_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX usuarios_usuariosico_contrato_id_like ON usuarios_usuariosico USING btree (contrato_id varchar_pattern_ops);


--
-- TOC entry 2359 (class 2606 OID 28074)
-- Name: auth_group_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2362 (class 2606 OID 28079)
-- Name: auth_user_groups_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2364 (class 2606 OID 28084)
-- Name: auth_user_user_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2366 (class 2606 OID 28089)
-- Name: auth_user_usuario_sico_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_usuario_sico
    ADD CONSTRAINT auth_user_usuario_sico_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2368 (class 2606 OID 28094)
-- Name: busquedas_vitacorabusquedas_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY busquedas_vitacorabusquedas
    ADD CONSTRAINT busquedas_vitacorabusquedas_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2371 (class 2606 OID 28099)
-- Name: calibreDeLaRed_id_refs_id_2c6e3024; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_actividad
    ADD CONSTRAINT "calibreDeLaRed_id_refs_id_2c6e3024" FOREIGN KEY ("calibreDeLaRed_id") REFERENCES ingresos_calibredelared(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2406 (class 2606 OID 28104)
-- Name: calle_id_refs_id_f08bb5af; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_ubicacion
    ADD CONSTRAINT calle_id_refs_id_f08bb5af FOREIGN KEY (calle_id) REFERENCES ingresos_calle(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2407 (class 2606 OID 28109)
-- Name: caserio_id_refs_id_0de611a2; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_ubicacion
    ADD CONSTRAINT caserio_id_refs_id_0de611a2 FOREIGN KEY (caserio_id) REFERENCES ingresos_caserio(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2372 (class 2606 OID 28114)
-- Name: claseRed_id_refs_id_19c1f11a; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_actividad
    ADD CONSTRAINT "claseRed_id_refs_id_19c1f11a" FOREIGN KEY ("claseRed_id") REFERENCES ingresos_clasered(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2361 (class 2606 OID 28119)
-- Name: content_type_id_refs_id_d043b34a; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT content_type_id_refs_id_d043b34a FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2417 (class 2606 OID 28124)
-- Name: contrato_id_refs_id_6be94172; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_medidor
    ADD CONSTRAINT contrato_id_refs_id_6be94172 FOREIGN KEY (contrato_id) REFERENCES inventario_detallematerialcontrato(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2373 (class 2606 OID 28129)
-- Name: demanda_id_refs_id_e90a6b0e; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_actividad
    ADD CONSTRAINT demanda_id_refs_id_e90a6b0e FOREIGN KEY (demanda_id) REFERENCES ingresos_demanda(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2420 (class 2606 OID 28134)
-- Name: detalleMaterialContrato_id_refs_id_92bcb22f; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_rangodematerial
    ADD CONSTRAINT "detalleMaterialContrato_id_refs_id_92bcb22f" FOREIGN KEY ("detalleMaterialContrato_id") REFERENCES inventario_detallematerialcontrato(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2421 (class 2606 OID 28139)
-- Name: detalleMaterialContrato_id_refs_id_cfae1324; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_sello
    ADD CONSTRAINT "detalleMaterialContrato_id_refs_id_cfae1324" FOREIGN KEY ("detalleMaterialContrato_id") REFERENCES inventario_detallematerialcontrato(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2369 (class 2606 OID 28144)
-- Name: django_admin_log_content_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_fkey FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2370 (class 2606 OID 28149)
-- Name: django_admin_log_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2374 (class 2606 OID 28154)
-- Name: estadoDeLaInstalacion_id_refs_id_13b86257; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_actividad
    ADD CONSTRAINT "estadoDeLaInstalacion_id_refs_id_13b86257" FOREIGN KEY ("estadoDeLaInstalacion_id") REFERENCES ingresos_estadodeunainstalacion(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2375 (class 2606 OID 28159)
-- Name: formaDeConexion_id_refs_id_fba03bc9; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_actividad
    ADD CONSTRAINT "formaDeConexion_id_refs_id_fba03bc9" FOREIGN KEY ("formaDeConexion_id") REFERENCES ingresos_formadeconexion(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2360 (class 2606 OID 28164)
-- Name: group_id_refs_id_f4b32aac; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT group_id_refs_id_f4b32aac FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2376 (class 2606 OID 28169)
-- Name: ingresos_actividad_cliente_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_actividad
    ADD CONSTRAINT ingresos_actividad_cliente_id_fkey FOREIGN KEY (cliente_id) REFERENCES ingresos_cliente(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2387 (class 2606 OID 28174)
-- Name: ingresos_canton_provincia_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_canton
    ADD CONSTRAINT ingresos_canton_provincia_id_fkey FOREIGN KEY (provincia_id) REFERENCES ingresos_provincia(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2388 (class 2606 OID 28179)
-- Name: ingresos_cliente_geocodigo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_cliente
    ADD CONSTRAINT ingresos_cliente_geocodigo_id_fkey FOREIGN KEY (geocodigo_id) REFERENCES ingresos_secuencia(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2390 (class 2606 OID 28184)
-- Name: ingresos_detalleclientemedidor_cliente_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_detalleclientemedidor
    ADD CONSTRAINT ingresos_detalleclientemedidor_cliente_id_fkey FOREIGN KEY (cliente_id) REFERENCES ingresos_cliente(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2392 (class 2606 OID 28189)
-- Name: ingresos_detalleclientereferencia_cliente_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_detalleclientereferencia
    ADD CONSTRAINT ingresos_detalleclientereferencia_cliente_id_fkey FOREIGN KEY (cliente_id) REFERENCES ingresos_cliente(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2393 (class 2606 OID 28194)
-- Name: ingresos_detalleclientereferencia_referencia_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_detalleclientereferencia
    ADD CONSTRAINT ingresos_detalleclientereferencia_referencia_id_fkey FOREIGN KEY (referencia_id) REFERENCES ingresos_cliente(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2395 (class 2606 OID 28199)
-- Name: ingresos_detalledeactividad_actividad_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_detalledeactividad
    ADD CONSTRAINT ingresos_detalledeactividad_actividad_id_fkey FOREIGN KEY (actividad_id) REFERENCES ingresos_actividad(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2397 (class 2606 OID 28204)
-- Name: ingresos_foto_actividad_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_foto
    ADD CONSTRAINT ingresos_foto_actividad_id_fkey FOREIGN KEY (actividad_id) REFERENCES ingresos_actividad(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2398 (class 2606 OID 28209)
-- Name: ingresos_instalador_cuadrilla_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_instalador
    ADD CONSTRAINT ingresos_instalador_cuadrilla_id_fkey FOREIGN KEY (cuadrilla_id) REFERENCES ingresos_cuadrilla(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2399 (class 2606 OID 28214)
-- Name: ingresos_instalador_nombre_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_instalador
    ADD CONSTRAINT ingresos_instalador_nombre_id_fkey FOREIGN KEY (nombre_id) REFERENCES ingresos_empleado(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2400 (class 2606 OID 28219)
-- Name: ingresos_materialdeactividad_actividad_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_materialdeactividad
    ADD CONSTRAINT ingresos_materialdeactividad_actividad_id_fkey FOREIGN KEY (actividad_id) REFERENCES ingresos_actividad(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2402 (class 2606 OID 28224)
-- Name: ingresos_parroquia_canton_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_parroquia
    ADD CONSTRAINT ingresos_parroquia_canton_id_fkey FOREIGN KEY (canton_id) REFERENCES ingresos_canton(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2403 (class 2606 OID 28229)
-- Name: ingresos_ruta_sector_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_ruta
    ADD CONSTRAINT ingresos_ruta_sector_id_fkey FOREIGN KEY (sector_id) REFERENCES ingresos_sector(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2404 (class 2606 OID 28234)
-- Name: ingresos_sector_canton_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_sector
    ADD CONSTRAINT ingresos_sector_canton_id_fkey FOREIGN KEY (canton_id) REFERENCES ingresos_canton(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2405 (class 2606 OID 28239)
-- Name: ingresos_secuencia_ruta_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_secuencia
    ADD CONSTRAINT ingresos_secuencia_ruta_id_fkey FOREIGN KEY (ruta_id) REFERENCES ingresos_ruta(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2408 (class 2606 OID 28244)
-- Name: ingresos_ubicacion_parroquia_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_ubicacion
    ADD CONSTRAINT ingresos_ubicacion_parroquia_id_fkey FOREIGN KEY (parroquia_id) REFERENCES ingresos_parroquia(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2411 (class 2606 OID 28249)
-- Name: ingresos_usoespecificodelinmueble_usoGeneral_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_usoespecificodelinmueble
    ADD CONSTRAINT "ingresos_usoespecificodelinmueble_usoGeneral_id_fkey" FOREIGN KEY ("usoGeneral_id") REFERENCES ingresos_usogeneraldelinmueble(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2377 (class 2606 OID 28254)
-- Name: instalador_id_refs_id_7cec5fdf; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_actividad
    ADD CONSTRAINT instalador_id_refs_id_7cec5fdf FOREIGN KEY (instalador_id) REFERENCES ingresos_instalador(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2409 (class 2606 OID 28259)
-- Name: interseccion_id_refs_id_f08bb5af; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_ubicacion
    ADD CONSTRAINT interseccion_id_refs_id_f08bb5af FOREIGN KEY (interseccion_id) REFERENCES ingresos_calle(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2412 (class 2606 OID 28264)
-- Name: inventario_detallematerialcontrato_contrato_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_detallematerialcontrato
    ADD CONSTRAINT inventario_detallematerialcontrato_contrato_id_fkey FOREIGN KEY (contrato_id) REFERENCES inventario_contrato(num) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2413 (class 2606 OID 28269)
-- Name: inventario_detallematerialcontrato_material_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_detallematerialcontrato
    ADD CONSTRAINT inventario_detallematerialcontrato_material_id_fkey FOREIGN KEY (material_id) REFERENCES inventario_subtipodematerial(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2414 (class 2606 OID 28274)
-- Name: inventario_detallerubro_contrato_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_detallerubro
    ADD CONSTRAINT inventario_detallerubro_contrato_id_fkey FOREIGN KEY (contrato_id) REFERENCES inventario_contrato(num) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2415 (class 2606 OID 28279)
-- Name: inventario_detallerubro_rubro_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_detallerubro
    ADD CONSTRAINT inventario_detallerubro_rubro_id_fkey FOREIGN KEY (rubro_id) REFERENCES inventario_rubro(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2416 (class 2606 OID 28284)
-- Name: inventario_detallerubro_servicio_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_detallerubro
    ADD CONSTRAINT inventario_detallerubro_servicio_id_fkey FOREIGN KEY (servicio_id) REFERENCES inventario_servicio(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2418 (class 2606 OID 28289)
-- Name: inventario_medidor_marca_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_medidor
    ADD CONSTRAINT inventario_medidor_marca_id_fkey FOREIGN KEY (marca_id) REFERENCES inventario_marca(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2419 (class 2606 OID 28294)
-- Name: inventario_medidor_modelo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_medidor
    ADD CONSTRAINT inventario_medidor_modelo_id_fkey FOREIGN KEY (modelo_id) REFERENCES ingresos_modelodemedidor(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2401 (class 2606 OID 28299)
-- Name: material_id_refs_id_1d2dd526; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_materialdeactividad
    ADD CONSTRAINT material_id_refs_id_1d2dd526 FOREIGN KEY (material_id) REFERENCES inventario_detallematerialcontrato(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2423 (class 2606 OID 28304)
-- Name: material_id_refs_id_93530002; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_tipodematerial
    ADD CONSTRAINT material_id_refs_id_93530002 FOREIGN KEY (material_id) REFERENCES inventario_material(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2391 (class 2606 OID 28309)
-- Name: medidor_id_refs_id_fe4999b2; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_detalleclientemedidor
    ADD CONSTRAINT medidor_id_refs_id_fe4999b2 FOREIGN KEY (medidor_id) REFERENCES inventario_medidor(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2378 (class 2606 OID 28314)
-- Name: motivoDeSolicitud_id_refs_id_c6f50055; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_actividad
    ADD CONSTRAINT "motivoDeSolicitud_id_refs_id_c6f50055" FOREIGN KEY ("motivoDeSolicitud_id") REFERENCES ingresos_motivoparasolicitud(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2379 (class 2606 OID 28319)
-- Name: nivelSocieconomico_id_refs_id_7cef28d2; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_actividad
    ADD CONSTRAINT "nivelSocieconomico_id_refs_id_7cef28d2" FOREIGN KEY ("nivelSocieconomico_id") REFERENCES ingresos_nivelsocieconomico(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2396 (class 2606 OID 28324)
-- Name: rubro_id_refs_id_81ae818f; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_detalledeactividad
    ADD CONSTRAINT rubro_id_refs_id_81ae818f FOREIGN KEY (rubro_id) REFERENCES inventario_detallerubro(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2380 (class 2606 OID 28329)
-- Name: tipoDeAcometidaRed_id_refs_id_007473a5; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_actividad
    ADD CONSTRAINT "tipoDeAcometidaRed_id_refs_id_007473a5" FOREIGN KEY ("tipoDeAcometidaRed_id") REFERENCES ingresos_tipodeacometidared(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2386 (class 2606 OID 28334)
-- Name: tipoDeCalle_id_refs_id_3b8b1af7; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_calle
    ADD CONSTRAINT "tipoDeCalle_id_refs_id_3b8b1af7" FOREIGN KEY ("tipoDeCalle_id") REFERENCES ingresos_tipocalle(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2381 (class 2606 OID 28339)
-- Name: tipoDeConstruccion_id_refs_id_4695fcf0; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_actividad
    ADD CONSTRAINT "tipoDeConstruccion_id_refs_id_4695fcf0" FOREIGN KEY ("tipoDeConstruccion_id") REFERENCES ingresos_tipodeconstruccion(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2422 (class 2606 OID 28344)
-- Name: tipoDeMaterial_id_refs_id_f6316418; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY inventario_subtipodematerial
    ADD CONSTRAINT "tipoDeMaterial_id_refs_id_f6316418" FOREIGN KEY ("tipoDeMaterial_id") REFERENCES inventario_tipodematerial(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2382 (class 2606 OID 28349)
-- Name: tipoDeSolicitud_id_refs_id_bdc4b5ab; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_actividad
    ADD CONSTRAINT "tipoDeSolicitud_id_refs_id_bdc4b5ab" FOREIGN KEY ("tipoDeSolicitud_id") REFERENCES ingresos_tipodesolicitud(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2383 (class 2606 OID 28354)
-- Name: ubicacionDelMedidor_id_refs_id_b054408a; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_actividad
    ADD CONSTRAINT "ubicacionDelMedidor_id_refs_id_b054408a" FOREIGN KEY ("ubicacionDelMedidor_id") REFERENCES ingresos_ubicaciondelmedidor(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2389 (class 2606 OID 28359)
-- Name: ubicacionGeografica_id_refs_id_2e830e6f; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_cliente
    ADD CONSTRAINT "ubicacionGeografica_id_refs_id_2e830e6f" FOREIGN KEY ("ubicacionGeografica_id") REFERENCES ingresos_ubicacion(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2394 (class 2606 OID 28364)
-- Name: ubicacion_id_refs_id_32be19ec; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_detalleclientereferencia
    ADD CONSTRAINT ubicacion_id_refs_id_32be19ec FOREIGN KEY (ubicacion_id) REFERENCES ingresos_ubicacion(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2410 (class 2606 OID 28369)
-- Name: urbanizacion_id_refs_id_a27f76e3; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_ubicacion
    ADD CONSTRAINT urbanizacion_id_refs_id_a27f76e3 FOREIGN KEY (urbanizacion_id) REFERENCES ingresos_urbanizacion(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2363 (class 2606 OID 28374)
-- Name: user_id_refs_id_40c41112; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT user_id_refs_id_40c41112 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2365 (class 2606 OID 28379)
-- Name: user_id_refs_id_4dc23c39; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT user_id_refs_id_4dc23c39 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2384 (class 2606 OID 28384)
-- Name: usoDeEnergia_id_refs_id_c06a88c2; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_actividad
    ADD CONSTRAINT "usoDeEnergia_id_refs_id_c06a88c2" FOREIGN KEY ("usoDeEnergia_id") REFERENCES ingresos_usodeenergia(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2385 (class 2606 OID 28389)
-- Name: usoEspecificoDelInmueble_id_refs_id_0f8f46bb; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ingresos_actividad
    ADD CONSTRAINT "usoEspecificoDelInmueble_id_refs_id_0f8f46bb" FOREIGN KEY ("usoEspecificoDelInmueble_id") REFERENCES ingresos_usoespecificodelinmueble(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2424 (class 2606 OID 28394)
-- Name: usuarios_usuariosico_contrato_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY usuarios_usuariosico
    ADD CONSTRAINT usuarios_usuariosico_contrato_id_fkey FOREIGN KEY (contrato_id) REFERENCES inventario_contrato(num) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2367 (class 2606 OID 28399)
-- Name: usuariosico_id_refs_id_1f26f244; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_usuario_sico
    ADD CONSTRAINT usuariosico_id_refs_id_1f26f244 FOREIGN KEY (usuariosico_id) REFERENCES usuarios_usuariosico(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2633 (class 0 OID 0)
-- Dependencies: 6
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2014-11-24 21:07:02

--
-- PostgreSQL database dump complete
--

