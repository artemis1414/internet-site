PGDMP     /    0                y            web_application_db    13.3    13.3 
    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16394    web_application_db    DATABASE     o   CREATE DATABASE web_application_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Russian_Russia.1251';
 "   DROP DATABASE web_application_db;
                postgres    false            �            1259    16408    product    TABLE     �   CREATE TABLE public.product (
    id bigint NOT NULL,
    name text NOT NULL,
    description text NOT NULL,
    price integer NOT NULL,
    value integer NOT NULL
);
    DROP TABLE public.product;
       public         heap    postgres    false            �            1259    16406    product_id_seq    SEQUENCE     w   CREATE SEQUENCE public.product_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.product_id_seq;
       public          postgres    false    201            �           0    0    product_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.product_id_seq OWNED BY public.product.id;
          public          postgres    false    200            #           2604    16411 
   product id    DEFAULT     h   ALTER TABLE ONLY public.product ALTER COLUMN id SET DEFAULT nextval('public.product_id_seq'::regclass);
 9   ALTER TABLE public.product ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    200    201    201            �          0    16408    product 
   TABLE DATA           F   COPY public.product (id, name, description, price, value) FROM stdin;
    public          postgres    false    201   z	       �           0    0    product_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.product_id_seq', 1, false);
          public          postgres    false    200            �      x������ � �     