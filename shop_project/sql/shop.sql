/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2018/8/2 ÐÇÆÚËÄ 10:36:20                        */
/*==============================================================*/


drop table if exists Relationship_14;

drop table if exists Relationship_23;

drop table if exists Relationship_7;

drop table if exists admin_handle_log;

drop table if exists admin_info;

drop table if exists admin_login_log;

drop table if exists admin_power;

drop table if exists admin_role;

drop table if exists amount_of_material;

drop table if exists emp_handle_log;

drop table if exists emp_info;

drop table if exists emp_login_log;

drop table if exists goods_info;

drop table if exists goods_type;

drop table if exists material_info;

drop table if exists material_type;

drop table if exists merchant_info;

drop table if exists recipe;

drop table if exists simulator_data;

drop table if exists store_info;

drop table if exists store_power;

drop table if exists store_role;

drop table if exists taste_type;

/*==============================================================*/
/* Table: Relationship_14                                       */
/*==============================================================*/
create table Relationship_14
(
   taste_type_id        int not null,
   goods_id             int not null,
   primary key (taste_type_id, goods_id)
);

/*==============================================================*/
/* Table: Relationship_23                                       */
/*==============================================================*/
create table Relationship_23
(
   admin_power_id       int not null,
   admin_role_id        int not null,
   primary key (admin_power_id, admin_role_id)
);

/*==============================================================*/
/* Table: Relationship_7                                        */
/*==============================================================*/
create table Relationship_7
(
   store_power_id       int not null,
   store_role_id        int not null,
   primary key (store_power_id, store_role_id)
);

/*==============================================================*/
/* Table: admin_handle_log                                      */
/*==============================================================*/
create table admin_handle_log
(
   admin_hadle_log_id   int not null auto_increment,
   admin_id             int,
   handle_time          datetime not null,
   event                varchar(256) not null,
   primary key (admin_hadle_log_id)
);

/*==============================================================*/
/* Table: admin_info                                            */
/*==============================================================*/
create table admin_info
(
   admin_id             int not null auto_increment,
   admin_role_id        int,
   name                 varchar(64) not null,
   leader_id            int,
   create_time          datetime not null,
   is_delete            bool not null,
   password             varchar(128) not null,
   last_time            datetime,
   sex                  bool not null,
   age                  int,
   phone_num            varchar(11) not null,
   email                varchar(64),
   primary key (admin_id)
);

/*==============================================================*/
/* Table: admin_login_log                                       */
/*==============================================================*/
create table admin_login_log
(
   admin_login_id       int not null auto_increment,
   admin_id             int,
   login_time           datetime not null,
   login_ip             varchar(64) not null,
   primary key (admin_login_id)
);

/*==============================================================*/
/* Table: admin_power                                           */
/*==============================================================*/
create table admin_power
(
   admin_power_id       int not null auto_increment,
   name                 varchar(64) not null,
   description          varchar(256) not null,
   primary key (admin_power_id)
);

/*==============================================================*/
/* Table: admin_role                                            */
/*==============================================================*/
create table admin_role
(
   admin_role_id        int not null auto_increment,
   name                 varchar(64) not null,
   is_delete            bool not null,
   create_time          datetime not null,
   description          varchar(256) not null,
   primary key (admin_role_id)
);

/*==============================================================*/
/* Table: amount_of_material                                    */
/*==============================================================*/
create table amount_of_material
(
   amount_id            int not null auto_increment,
   material_info_id     int,
   time                 datetime not null,
   amount_of_use        int not null,
   primary key (amount_id)
);

/*==============================================================*/
/* Table: emp_handle_log                                        */
/*==============================================================*/
create table emp_handle_log
(
   emp_handle_log_id    int not null auto_increment,
   emp_id               int,
   handle_time          datetime not null,
   event                varchar(256) not null,
   primary key (emp_handle_log_id)
);

/*==============================================================*/
/* Table: emp_info                                              */
/*==============================================================*/
create table emp_info
(
   emp_id               int not null auto_increment,
   store_info_id        int,
   store_role_id        int,
   name                 varchar(64) not null,
   emp_no               varchar(64),
   sex                  bool not null,
   age                  int,
   join_time            datetime,
   work_status          varchar(32),
   salary               int,
   subsidy              int,
   work_time            int,
   password             varchar(128) not null,
   primary key (emp_id)
);

/*==============================================================*/
/* Table: emp_login_log                                         */
/*==============================================================*/
create table emp_login_log
(
   emp_login_id         int not null auto_increment,
   merchant_id          int,
   emp_id               int,
   longin_time          datetime not null,
   login_ip             varchar(64) not null,
   primary key (emp_login_id)
);

/*==============================================================*/
/* Table: goods_info                                            */
/*==============================================================*/
create table goods_info
(
   goods_id             int not null auto_increment,
   store_info_id        int,
   goods_type_id        int,
   name                 varchar(64) not null,
   price                int not null,
   primary key (goods_id)
);

/*==============================================================*/
/* Table: goods_type                                            */
/*==============================================================*/
create table goods_type
(
   goods_type_id        int not null auto_increment,
   name                 varchar(64) not null,
   primary key (goods_type_id)
);

/*==============================================================*/
/* Table: material_info                                         */
/*==============================================================*/
create table material_info
(
   material_info_id     int not null auto_increment,
   material_type_id     int,
   name                 varchar(64) not null,
   primary key (material_info_id)
);

/*==============================================================*/
/* Table: material_type                                         */
/*==============================================================*/
create table material_type
(
   material_type_id     int not null auto_increment,
   merchant_id          int,
   name                 varchar(64) not null,
   create_time          datetime not null,
   emp_id               int not null,
   is_delete            bool not null,
   primary key (material_type_id)
);

/*==============================================================*/
/* Table: merchant_info                                         */
/*==============================================================*/
create table merchant_info
(
   merchant_id          int not null auto_increment,
   name                 varchar(64) not null,
   password             varchar(128) not null,
   sex                  bool,
   icon                 varchar(64),
   email                varchar(64),
   phone_number         varchar(11) not null,
   address              varchar(128),
   primary key (merchant_id)
);

/*==============================================================*/
/* Table: recipe                                                */
/*==============================================================*/
create table recipe
(
   recipe_id            int not null auto_increment,
   goods_id             int,
   material_info_id     int,
   need_count           int not null,
   unit                 varchar(32) not null,
   primary key (recipe_id)
);

/*==============================================================*/
/* Table: simulator_data                                        */
/*==============================================================*/
create table simulator_data
(
   simulator_data_id    int not null auto_increment,
   goods_id             int not null,
   name                 varchar(64) not null,
   score                real not null,
   place                varchar(128) not null,
   sole_time            datetime not null,
   type_goods           int not null,
   type_taste           int not null,
   t_price              int not null,
   create_time          datetime not null,
   update_time          datetime not null,
   merchant_name        varchar(64) not null,
   primary key (simulator_data_id)
);

/*==============================================================*/
/* Table: store_info                                            */
/*==============================================================*/
create table store_info
(
   store_info_id        int not null auto_increment,
   merchant_id          int,
   name                 varchar(64) not null,
   address              varchar(128) not null,
   primary key (store_info_id)
);

/*==============================================================*/
/* Table: store_power                                           */
/*==============================================================*/
create table store_power
(
   store_power_id       int not null auto_increment,
   name                 varchar(64) not null,
   primary key (store_power_id)
);

/*==============================================================*/
/* Table: store_role                                            */
/*==============================================================*/
create table store_role
(
   store_role_id        int not null auto_increment,
   name                 varchar(64) not null,
   primary key (store_role_id)
);

/*==============================================================*/
/* Table: taste_type                                            */
/*==============================================================*/
create table taste_type
(
   taste_type_id        int not null auto_increment,
   taste                varchar(128) not null,
   sales                int not null,
   score                real not null,
   create_time          datetime not null,
   update_time          datetime not null,
   primary key (taste_type_id)
);

alter table Relationship_14 add constraint FK_Relationship_15 foreign key (goods_id)
      references goods_info (goods_id) on delete restrict on update restrict;

alter table Relationship_14 add constraint FK_Relationship_16 foreign key (taste_type_id)
      references taste_type (taste_type_id) on delete restrict on update restrict;

alter table Relationship_23 add constraint FK_Relationship_24 foreign key (admin_role_id)
      references admin_role (admin_role_id) on delete restrict on update restrict;

alter table Relationship_23 add constraint FK_Relationship_25 foreign key (admin_power_id)
      references admin_power (admin_power_id) on delete restrict on update restrict;

alter table Relationship_7 add constraint FK_Relationship_8 foreign key (store_role_id)
      references store_role (store_role_id) on delete restrict on update restrict;

alter table Relationship_7 add constraint FK_Relationship_9 foreign key (store_power_id)
      references store_power (store_power_id) on delete restrict on update restrict;

alter table admin_handle_log add constraint FK_Relationship_20 foreign key (admin_id)
      references admin_info (admin_id) on delete restrict on update restrict;

alter table admin_info add constraint FK_Relationship_21 foreign key (admin_role_id)
      references admin_role (admin_role_id) on delete restrict on update restrict;

alter table admin_login_log add constraint FK_Relationship_22 foreign key (admin_id)
      references admin_info (admin_id) on delete restrict on update restrict;

alter table amount_of_material add constraint FK_Relationship_19 foreign key (material_info_id)
      references material_info (material_info_id) on delete restrict on update restrict;

alter table emp_handle_log add constraint FK_Relationship_10 foreign key (emp_id)
      references emp_info (emp_id) on delete restrict on update restrict;

alter table emp_info add constraint FK_Relationship_2 foreign key (store_info_id)
      references store_info (store_info_id) on delete restrict on update restrict;

alter table emp_info add constraint FK_Relationship_6 foreign key (store_role_id)
      references store_role (store_role_id) on delete restrict on update restrict;

alter table emp_login_log add constraint FK_Relationship_11 foreign key (emp_id)
      references emp_info (emp_id) on delete restrict on update restrict;

alter table emp_login_log add constraint FK_Relationship_3 foreign key (merchant_id)
      references merchant_info (merchant_id) on delete restrict on update restrict;

alter table goods_info add constraint FK_Relationship_12 foreign key (goods_type_id)
      references goods_type (goods_type_id) on delete restrict on update restrict;

alter table goods_info add constraint FK_Relationship_5 foreign key (store_info_id)
      references store_info (store_info_id) on delete restrict on update restrict;

alter table material_info add constraint FK_Relationship_18 foreign key (material_type_id)
      references material_type (material_type_id) on delete restrict on update restrict;

alter table material_type add constraint FK_Relationship_4 foreign key (merchant_id)
      references merchant_info (merchant_id) on delete restrict on update restrict;

alter table recipe add constraint FK_Relationship_13 foreign key (goods_id)
      references goods_info (goods_id) on delete restrict on update restrict;

alter table recipe add constraint FK_Relationship_17 foreign key (material_info_id)
      references material_info (material_info_id) on delete restrict on update restrict;

alter table store_info add constraint FK_Relationship_1 foreign key (merchant_id)
      references merchant_info (merchant_id) on delete restrict on update restrict;

