INSERT INTO public."user"
(created_at, updated_at, email, "password", username, is_active, is_superuser, "type")
VALUES(now(), now(), 'daniel@gmail.com', '$2a$12$CqysGTzoWRUgy21aEEV5LOmX8EVGZsLgHSLUwNI0GybXukcIS/s7.', 'daniel', true, true, 'user');


ALTER TABLE infraction
ADD CONSTRAINT fk_vehicle_id
FOREIGN KEY (vehicle_id) REFERENCES vehicle(id);

ALTER TABLE infraction
ADD CONSTRAINT fk_vehicle_id
FOREIGN KEY (police_id) REFERENCES police(id);


CREATE OR REPLACE function sp_get_report_by_email("pEmail" varchar)
    RETURNS TABLE
            (
                "reportName" varchar,
                "reportCarPlate" varchar,
                "reportModel" varchar,
                "reportColor" varchar,
                "reportCommet" varchar,
                "reportDate" varchar
            )
AS
$BODY$
DECLARE
    P_EMAIL ALIAS FOR $1;
BEGIN
    RETURN QUERY
    select
	    p."name" as reportName,
	    v.car_plate as reportCarPlate,
	    v.model as reportModel,
	    v.color as reportColor,
	    inf."comments" as reportCommet,
	    TO_CHAR(inf.created_at, 'YYYY-MM-DD HH24:MI:SS')::varchar as reportDate
    from "user" u
	inner join police p on p.user_id = u.id
	left join infraction inf on inf.police_id = p.id
	inner join vehicle v on v.id= inf.vehicle_id
	where u.email = P_EMAIL;
END ;
$BODY$
    LANGUAGE plpgsql VOLATILE
                     COST 100
                     ROWS 1000;
