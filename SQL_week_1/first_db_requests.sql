SELECT name, Year, ALIGN, FIRST_APPEARANCE, APPEARANCES
FROM MarvelCharacters
WHERE HAIR = 'Bald'
    AND ALIGN = 'Bad Characters'
    AND Year BETWEEN 1990 AND 1999
    AND Year IS NOT NULL
ORDER BY APPEARANCES DESC;

SELECT name, identify, FIRST_APPEARANCE, EYE
FROM MarvelCharacters
WHERE identify = 'Secret Identity'
    AND EYE NOT IN ('Blue Eyes', 'Brown Eyes', 'Green Eyes')
    AND FIRST_APPEARANCE IS NOT NULL
ORDER BY FIRST_APPEARANCE ASC;

SELECT name, HAIR
FROM MarvelCharacters
WHERE HAIR = 'Variable Hair';

SELECT name, SEX, EYE
FROM MarvelCharacters
WHERE SEX = 'Female Characters'
    AND EYE IN ('Gold Eyes', 'Amber Eyes');

SELECT name, Year, FIRST_APPEARANCE, identify
FROM MarvelCharacters
WHERE identify = 'No Dual Identity'
ORDER BY Year DESC;

SELECT name, ALIGN, HAIR
FROM MarvelCharacters
WHERE ALIGN IN ('Bad Characters', 'Good Characters')
    AND HAIR NOT IN ('Brown Hair', 'Black Hair', 'Blond Hair', 'Red Hair');

SELECT name, Year
FROM MarvelCharacters
WHERE Year BETWEEN 1960 AND 1969;

SELECT name, EYE, HAIR
FROM MarvelCharacters
WHERE EYE = 'Yellow Eyes'
    AND HAIR = 'Red Hair';

SELECT name, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES < 10
ORDER BY APPEARANCES DESC;

