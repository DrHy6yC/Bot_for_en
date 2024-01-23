DROP PROCEDURE IF EXISTS get_is_user_in_bd;
DELIMITER //
CREATE PROCEDURE get_is_user_in_bd(IN user_tg INT, OUT is_user_in_bd INT)
BEGIN
	DECLARE id_user INT;
	SELECT USER_TG_ID INTO id_user FROM USERS
	WHERE USER_TG_ID = user_tg;
    IF id_user IS NOT NULL
		THEN SET is_user_in_bd = 1;
        ELSE SET is_user_in_bd = 0;
    END IF;
END//

-------------------------------------------
