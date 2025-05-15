SELECT ALIVE, COUNT(*)
FROM MarvelCharacters
GROUP BY ALIVE;

SELECT EYE, FLOOR(AVG(APPEARANCES))
FROM MarvelCharacters
GROUP BY EYE;

SELECT HAIR, MAX(APPEARANCES)
FROM MarvelCharacters
GROUP BY HAIR;

SELECT identify, min(APPEARANCES)
FROM MarvelCharacters
WHERE identify = 'Public Identity'
GROUP BY identify;

SELECT SEX, COUNT(*)
FROM MarvelCharacters
GROUP BY SEX;

SELECT DISTINCT identify, FLOOR(AVG(Year))
FROM MarvelCharacters
GROUP BY identify;

SELECT DISTINCT EYE, ALIVE, COUNT(*)
FROM MarvelCharacters
WHERE ALIVE = 'Living Characters'
GROUP BY EYE;

SELECT HAIR, MAX(APPEARANCES), MIN(APPEARANCES)
FROM MarvelCharacters
GROUP BY HAIR;

SELECT identify, ALIVE, COUNT(*)
FROM MarvelCharacters
WHERE ALIVE = 'Deceased Characters'
GROUP BY identify;

SELECT EYE, FLOOR(AVG(Year))
FROM MarvelCharacters
GROUP BY EYE;

SELECT name, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES = (
    SELECT MAX(APPEARANCES) FROM MarvelCharacters
);

SELECT name, Year
FROM MarvelCharacters
WHERE Year = (
    SELECT Year
    FROM MarvelCharacters
    WHERE APPEARANCES = (SELECT MAX(APPEARANCES) FROM MarvelCharacters)
    LIMIT 1
);

