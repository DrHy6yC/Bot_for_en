DROP PROCEDURE IF EXISTS get_is_user_in_bd;
DELIMITER //
CREATE PROCEDURE get_is_user_in_bd(
IN user_tg BIGINT,
OUT is_user_in_bd BIT)
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
DROP PROCEDURE IF EXISTS set_user_in_bd;
DELIMITER //
CREATE PROCEDURE set_user_in_bd(
IN user_id BIGINT, IN user_name VARCHAR(50),
IN user_login_tg VARCHAR(30))
BEGIN
    INSERT INTO USERS (USER_TG_ID, USER_FULL_NAME, USER_LOGIN)
    VALUES (user_id, user_name, user_login_tg);
END//

-------------------------------------------
DROP PROCEDURE IF EXISTS get_const_db;
DELIMITER //
CREATE PROCEDURE get_const_db(
IN const_name VARCHAR(25),
OUT const_value VARCHAR(200))
BEGIN
    SELECT CONSTANT_VALUES INTO const_value FROM CONSTANTS
WHERE CONSTANT_NAMES = const_name;
END//

-------------------------------------------
DROP PROCEDURE IF EXISTS get_id_survey_db;
DELIMITER //
CREATE PROCEDURE get_id_survey_db(
IN name_survey VARCHAR(50),
OUT id_survey INT)
BEGIN
    SELECT SURVEY_ID INTO id_survey FROM SURVEYS
    WHERE SURVEY_NAME = name_survey;
END//

-------------------------------------------
DROP PROCEDURE IF EXISTS get_answer;
DELIMITER //
CREATE PROCEDURE get_answer(
IN num_question INT,
IN id_survey INT)
BEGIN

    SELECT ANSWER FROM SURVEYS_ANSWERS
    WHERE NUMBER_QUESTION = num_question and SURVEY_ID = id_survey;
END//

-------------------------------------------
DROP PROCEDURE IF EXISTS get_question;
DELIMITER //
CREATE PROCEDURE get_question(
IN num_question INT,
IN id_survey INT,
OUT question_txt VARCHAR(200))
BEGIN
    SELECT SURVEY_QUESTION INTO question_txt FROM SURVEYS_QUESTIONS
    WHERE NUMBER_QUESTION = num_question and SURVEY_ID = id_survey;
END//


-------------------------------------------
DROP PROCEDURE IF EXISTS get_one_answer;
DELIMITER //
CREATE PROCEDURE get_one_answer(
IN num_question INT,
IN id_survey INT,
IN num_answer INT,
OUT answer_txt VARCHAR(200))
BEGIN
    SELECT ANSWER INTO answer_txt FROM SURVEYS_ANSWERS
    WHERE NUMBER_QUESTION = num_question and SURVEY_ID = id_survey and NUMBER_ANSWER = num_answer;
END//


-------------------------------------------
DROP PROCEDURE IF EXISTS get_name_survey;
DELIMITER //
CREATE PROCEDURE get_name_survey()
BEGIN
    SELECT SURVEY_NAME FROM SURVEYS;
END//


-------------------------------------------
DROP PROCEDURE IF EXISTS set_survey_name_get_id_survey;
DELIMITER //
CREATE PROCEDURE set_survey_name_get_id_survey(
IN name_survey VARCHAR(50),
IN description_survey VARCHAR(500),
OUT id_survey INT)
BEGIN
    INSERT INTO SURVEYS (SURVEY_NAME, SURVEY_DESCRIPTION)
    VALUES (name_survey, description_survey);
    SELECT SURVEY_ID INTO id_survey FROM SURVEYS
    WHERE SURVEY_NAME = name_survey;
END//


-------------------------------------------
DROP PROCEDURE IF EXISTS set_survey;
DELIMITER //
CREATE PROCEDURE set_survey(
IN id_survey INT,
IN num_question INT,
IN question VARCHAR(200),
IN answer_1 VARCHAR(200),
IN answer_2 VARCHAR(200),
IN answer_3 VARCHAR(200),
IN answer_4 VARCHAR(200),
IN true_answer INT)
BEGIN
    INSERT INTO SURVEYS_QUESTIONS (SURVEY_ID, NUMBER_QUESTION, SURVEY_QUESTION)
     VALUES (id_survey, num_question, question);
    INSERT INTO SURVEYS_TRUE_ANSWERS (SURVEY_ID, NUMBER_QUESTION, NUMBER_TRUE_ANSWER)
     VALUES (id_survey, num_question, true_answer);
    INSERT INTO SURVEYS_ANSWERS (NUMBER_ANSWER, SURVEY_ID, NUMBER_QUESTION, ANSWER)
     VALUES (1, id_survey, num_question, answer_1);
    INSERT INTO SURVEYS_ANSWERS (NUMBER_ANSWER, SURVEY_ID, NUMBER_QUESTION, ANSWER)
     VALUES (2, id_survey, num_question, answer_2);
    INSERT INTO SURVEYS_ANSWERS (NUMBER_ANSWER, SURVEY_ID, NUMBER_QUESTION, ANSWER)
     VALUES (3, id_survey, num_question, answer_3);
    INSERT INTO SURVEYS_ANSWERS (NUMBER_ANSWER, SURVEY_ID, NUMBER_QUESTION, ANSWER)
     VALUES (4, id_survey, num_question, answer_4);
END//
