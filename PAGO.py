CREATE TABLE table_name
(
col1 datatype [ NULL | NOT NULL ],
col2 datatype [ NULL | NOT NULL ],
...
col_n datatype [ NULL | NOT NULL ]
constraint <name> FOREIGN KEY (col1,col2) REFERENCES table(col1,col2)
)  tablespace <tablepace name>

CREATE TABLE table_name
(
col1 datatype [ NULL | NOT NULL ] constraint <name> primary key
,
col2 datatype [ NULL | NOT NULL ],
...
col_n datatype [ NULL | NOT NULL ]
)  tablespace <tablepace name>;

CREATE TABLE dept
( dept_id number(10) NOT NULL,
dept_name varchar2(50) NOT NULL,
CONSTRAINT dept_pk PRIMARY KEY (dept_id)
);
