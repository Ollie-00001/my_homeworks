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

