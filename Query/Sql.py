win_rate =  """
                WITH
          temp1 AS(
          SELECT
            hero_id,
            ROUND(COUNT(
              IF
                (win=1,
                  TRUE,
                  NULL)) / COUNT(*) * 100, 2) AS RATE
          FROM
            `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS`
          GROUP BY
            1
          ORDER BY
            2 DESC),
          temp2 AS(
          SELECT
            a.hero_id,
            a.RATE,
            b.localized_name
          FROM
            temp1 AS a
          INNER JOIN
            `personal-project-for-dota2.DOTA2_MATCH.hero_names` AS b
          ON
            a.hero_id = b.hero_id
          ORDER BY
            2 DESC
          LIMIT
            5),
          temp3 AS(
          SELECT
            a.hero_id,
            a.RATE,
            b.localized_name
          FROM
            temp1 AS a
          INNER JOIN
            `personal-project-for-dota2.DOTA2_MATCH.hero_names` AS b
          ON
            a.hero_id = b.hero_id
          ORDER BY
            2
          LIMIT
            5)
        SELECT
          *
        FROM
          temp2
        UNION ALL
        SELECT
          *
        FROM
          temp3
        ORDER BY RATE DESC
    """

win_rate_top30 = """
WITH
  temp1 AS(
  SELECT
    hero_id,
    ROUND(COUNT(
      IF
        (win=1,
          TRUE,
          NULL)) / COUNT(*) * 100, 2) AS RATE
  FROM
    `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS`
  GROUP BY
    1
  ORDER BY
    2 DESC),
  temp2 AS(
  SELECT
    a.hero_id,
    a.RATE,
    b.localized_name
  FROM
    temp1 AS a
  INNER JOIN
    `personal-project-for-dota2.DOTA2_MATCH.hero_names` AS b
  ON
    a.hero_id = b.hero_id
  ORDER BY
    2 DESC
  LIMIT
    15),
  temp3 AS(
  SELECT
    a.hero_id,
    a.RATE,
    b.localized_name
  FROM
    temp1 AS a
  INNER JOIN
    `personal-project-for-dota2.DOTA2_MATCH.hero_names` AS b
  ON
    a.hero_id = b.hero_id
  ORDER BY
    2
  LIMIT
    15)
SELECT
  *
FROM
  temp2
UNION ALL
SELECT
  *
FROM
  temp3
ORDER BY
  RATE DESC
    """

win_avg = """
    WITH temp1 as(
    SELECT
      hero_id,
      ROUND(COUNT(IF(win=1, TRUE, NULL)) / COUNT(*) * 100 , 2) AS RATE
    FROM
      `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS`

    GROUP BY 1
    ORDER BY 2 DESC)

    SELECT ROUND(AVG(RATE), 2) as AVG
    FROM temp1
    """

use_rate = """
            WITH
          temp1 AS(
          SELECT
            hero_id,
            COUNT(*) AS match_all
          FROM
            `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS`
          GROUP BY
            1),
          temp2 AS(
          SELECT
            COUNT(DISTINCT match_id) AS all_match
          FROM
            `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS`),
          temp3 AS(
          SELECT
            a.hero_id,
            ROUND((a.match_all / b.all_match)*100, 2) AS use_rate
          FROM
            temp1 AS a,
            temp2 AS b
          ORDER BY
            2 DESC
          LIMIT
            5),
          temp4 AS(
          SELECT
            a.hero_id,
            ROUND((a.match_all / b.all_match)*100, 2) AS use_rate
          FROM
            temp1 AS a,
            temp2 AS b
          ORDER BY
            2
          LIMIT
            5),
          temp5 AS(
          SELECT
            *
          FROM
            temp3
          UNION ALL
          SELECT
            *
          FROM
            temp4
          ORDER BY
            use_rate DESC)
        SELECT
          a.hero_id,
          a.use_rate,
          b.localized_name
        FROM
          temp5 AS a
        INNER JOIN
          `personal-project-for-dota2.DOTA2_MATCH.hero_names` AS b
        ON
          a.hero_id = b.hero_id
        ORDER BY
          2 DESC
    """

use_rate_30 = """
WITH
          temp1 AS(
          SELECT
            hero_id,
            COUNT(*) AS match_all
          FROM
            `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS`
          GROUP BY
            1),
          temp2 AS(
          SELECT
            COUNT(DISTINCT match_id) AS all_match
          FROM
            `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS`),
          temp3 AS(
          SELECT
            a.hero_id,
            ROUND((a.match_all / b.all_match)*100, 2) AS use_rate
          FROM
            temp1 AS a,
            temp2 AS b
          ORDER BY
            2 DESC
          LIMIT
            15),
          temp4 AS(
          SELECT
            a.hero_id,
            ROUND((a.match_all / b.all_match)*100, 2) AS use_rate
          FROM
            temp1 AS a,
            temp2 AS b
          ORDER BY
            2
          LIMIT
            15),
          temp5 AS(
          SELECT
            *
          FROM
            temp3
          UNION ALL
          SELECT
            *
          FROM
            temp4
          ORDER BY
            use_rate DESC)
        SELECT
          a.hero_id,
          a.use_rate,
          b.localized_name
        FROM
          temp5 AS a
        INNER JOIN
          `personal-project-for-dota2.DOTA2_MATCH.hero_names` AS b
        ON
          a.hero_id = b.hero_id
        ORDER BY
          2 DESC
"""

use_avg = """
                WITH
          temp1 AS(
          SELECT
            hero_id,
            COUNT(*) AS match_all
          FROM
            `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS`
          GROUP BY
            1),
          temp2 AS(
          SELECT
            COUNT(DISTINCT match_id) AS all_match
          FROM
            `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS`)
        SELECT
            ROUND(AVG((a.match_all / b.all_match)*100), 2) AS AVG
          FROM
            temp1 AS a,
            temp2 AS b
        """

gold_xp_min = """
        SELECT
          gold_or_xp,
          minute,
          value
        FROM
          `personal-project-for-dota2.DOTA2_MATCH.DOTA_ADVANTAGES`
        WHERE
          match_id = 5260163509
        ORDER BY
          minute
"""

analytic_temp = """
WITH temp1 AS(
SELECT  b.hero_id, ROUND(AVG(a. duration), 0) as avg_time
FROM `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  AS a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS` as b
ON a.match_id = b. match_id
AND (b.hero_id = 83 or b.hero_id = 32 or b.hero_id = 62
or b.hero_id = 61 or b.hero_id = 63 or b.hero_id = 56 or b.hero_id = 88)
GROUP BY 1),
temp2 AS(
SELECT hero_id,  ROUND(AVG(((kills+assists)/(deaths+1))), 2) AS kda,
ROUND(AVG(gold_per_min), 2) AS gold_per_min,
ROUND(AVG(xp_per_min), 2) AS xp_per_min,
ROUND(AVG(courier_kills), 2) AS courier_kills,
ROUND((COUNT(IF(win=1,true,null)) / COUNT(win)), 2) AS win_rate,
COUNT(DISTINCT match_id) as use
FROM `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS`
WHERE (hero_id = 83 or hero_id = 32 or hero_id = 62
or hero_id = 61 or hero_id = 63 or hero_id = 56 or hero_id = 88)
GROUP BY 1),
temp3 AS(
SELECT a.hero_id, COUNT(b.is_pick) as ban
FROM `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS`  as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_PICK_BANS` as b
ON a.match_id = b.match_id
AND is_pick = false
AND (a.hero_id = 83 or a.hero_id = 32 or a.hero_id = 62
or a.hero_id = 61 or a.hero_id = 63 or a.hero_id = 56 or a.hero_id = 88)
group by 1),
temp4 AS(
SELECT t1.hero_id as hero_id, t4.localized_name as hero_name, t1.avg_time as avg_time, t2.kda as kda, t2.gold_per_min as gold_per_min,
t2.xp_per_min as xp_per_min, t2.courier_kills as courier_kills, t2.win_rate as win_rate, t2,use as use, t3.ban as ban
FROM temp1 as t1,
temp2 as t2,
temp3 as t3,
`personal-project-for-dota2.DOTA2_MATCH.hero_names` as t4
WHERE t1.hero_id = t2.hero_id
AND t1.hero_id = t3.hero_id
AND t1.hero_id = t4.hero_id),
temp5 AS(
SELECT COUNT(DISTINCT match_id) AS all_match
FROM
`personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS`),
Good_data AS(
SELECT hero_id, ROUND(((0.4*(win_rate / 1 * 100)) + 0.35*(IF(kda>5, 100, kda/5*100)) + 0.25*(gold_per_min/2000 * 50 + xp_per_min/2000 * 50)), 2) as good_val, 
RANK() OVER (
ORDER BY ROUND(((0.4*(win_rate / 1 * 100)) + 0.35*(IF(kda>5, 100, kda/5*100)) + 0.25*(gold_per_min/2000 * 50 + xp_per_min/2000 * 50)), 2) DESC
)ranking
FROM temp4),
Opponent_headache AS(
SELECT hero_id, ROUND((0.7 * (ban/100000) * 100 + 0.3 * (courier_kills/1) * 100), 2) as headache_val, 
RANK() OVER (
ORDER BY ROUND((0.7 * (ban/100000) * 100 + 0.3 * (courier_kills/1) * 100), 2) DESC
)ranking
FROM temp4)
"""

analytic_1_get_useRate = """
SELECT t2.hero_id, ROUND(t2.use / t5.all_match * 100, 2) as use_rate
FROM temp2 as t2,
temp5 as t5
"""

analytic_1_get_avgBan = """
SELECT ROUND(AVG(t1.ban * 100 / t2.all_match), 2) as avg_ban
FROM(
SELECT COUNT(DISTINCT match_id) AS ban
FROM `personal-project-for-dota2.DOTA2_MATCH.DOTA_PICK_BANS` 
WHERE is_pick = false
GROUP BY hero_id) as t1, 
(SELECT count(DISTINCT match_id) as all_match
FROm `personal-project-for-dota2.DOTA2_MATCH.DOTA_PICK_BANS` 
WHERE is_pick = false) as t2
"""

analytic_1_get_banRate = """
SELECT hero_id, ROUND(t3.ban * 100 / t2.all_match, 2) as ban_rate
FROM temp3 as t3,
(SELECT count(DISTINCT match_id) as all_match
FROm `personal-project-for-dota2.DOTA2_MATCH.DOTA_PICK_BANS` 
WHERE is_pick = false) as t2
"""

analytic_1_get_good_data = """
SELECT *
FROM Good_data
ORDER BY ranking
"""

analytic_1_get_opponent_headache = """
SELECT *
FROM Opponent_headache
ORDER BY ranking
"""

analytic_2_useRate_faceValue = """
WITH temp1 AS(
SELECT hero_id, COUNT(*) as match_all
FROM `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS`
GROUP BY 1),
temp3 AS(
SELECT COUNT(DISTINCT match_id) as all_match
FROM `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS`)

SELECT c.localized_name, ROUND((a.match_all / d.all_match)*100, 2) as use_rate ,c.Face_value_score as face_value
FROM temp1 as a,
`personal-project-for-dota2.DOTA2_MATCH.hero_names`  as c,
temp3 as d
WHERE a.hero_id = c.hero_id
ORDER BY face_value DESC
"""

# rate in with bfury & without bfury
analytic_3_rate = """
SELECT COUNT(DISTINCT match_id) as val
FROM `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS` 
WHERE 
  hero_id = 1
  AND (item_0 = 145
    OR item_1 = 145
    OR item_2 = 145
    OR item_3 = 145
    OR item_4 = 145
    OR item_5 = 145)
UNION ALL 
SELECT COUNT(DISTINCT match_id) as val
FROM `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS` 
WHERE
  hero_id = 1
  AND (item_0 = 145
    AND item_1 != 145
    AND item_2 != 145
    AND item_3 != 145
    AND item_4 != 145
    AND item_5 != 145)
"""


#bfury win_rate
analytic_3_win_rate_bf = """
SELECT
  ROUND(COUNT(
    IF
      (win=1,
        TRUE,
        NULL)) / COUNT(win) * 100, 2) AS RATE
FROM
  `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS`
WHERE
  hero_id = 1
  AND (item_0 = 145
    AND item_1 != 145
    AND item_2 != 145
    AND item_3 != 145
    AND item_4 != 145
    AND item_5 != 145)
UNION ALL 
SELECT
  ROUND(COUNT(
    IF
      (win=1,
        TRUE,
        NULL)) / COUNT(win) * 100, 2) AS RATE
FROM
  `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS`
WHERE
  hero_id = 1
  AND (item_0 = 145
    OR item_1 = 145
    OR item_2 = 145
    OR item_3 = 145
    OR item_4 = 145
    OR item_5 = 145)
"""

#Without bfury win_rate
analytic_3_win_rate_without_bf = """
SELECT
  ROUND(COUNT(
    IF
      (win=1,
        TRUE,
        NULL)) / COUNT(win) * 100, 2) AS RATE
FROM
  `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS`
WHERE
  hero_id = 1
  AND (item_0 = 145
    AND item_1 != 145
    AND item_2 != 145
    AND item_3 != 145
    AND item_4 != 145
    AND item_5 != 145)
"""

#Time distribution with bfury
analytic_3_time_with_bf = """
SELECT count(IF(b.duration > 1000 AND b.duration <= 1640, TRUE, NULL)) as t1,
count(IF(b.duration > 1640 AND b.duration <= 2280, TRUE, NULL)) as t2,
count(IF(b.duration > 2280 AND b.duration <= 2920, TRUE, NULL)) as t3,
count(IF(b.duration > 2920 AND b.duration <= 3560, TRUE, NULL)) as t4,
count(IF(b.duration > 3560 AND b.duration <= 4200, TRUE, NULL)) as t5,
ROUND(SUM(b.duration) / COUNT(B.match_id), 2) as avg
FROM `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS`  as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.hero_id = 1
  AND (a.item_0 = 145
    OR a.item_1 = 145
    OR a.item_2 = 145
    OR a.item_3 = 145
    OR a.item_4 = 145
    OR a.item_5 = 145)
"""

#Time distribution without bfury
analytic_3_time_without_bf = """
SELECT count(IF(b.duration > 1000 AND b.duration <= 1640, TRUE, NULL)) as t1,
count(IF(b.duration > 1640 AND b.duration <= 2280, TRUE, NULL)) as t2,
count(IF(b.duration > 2280 AND b.duration <= 2920, TRUE, NULL)) as t3,
count(IF(b.duration > 2920 AND b.duration <= 3560, TRUE, NULL)) as t4,
count(IF(b.duration > 3560 AND b.duration <= 4200, TRUE, NULL)) as t5,
ROUND(SUM(b.duration) / COUNT(B.match_id), 2) as avg
FROM `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS`  as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.hero_id = 1
  AND (a.item_0 != 145
    AND a.item_1 != 145
    AND a.item_2 != 145
    AND a.item_3 != 145
    AND a.item_4 != 145
    AND a.item_5 != 145)
"""

#minute_buy_bfury
analytic_3_minute = """
WITH
  temp1 AS(
  SELECT
    DISTINCT a.match_id,
    c.time
  FROM
    `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS` AS a
  INNER JOIN
    `personal-project-for-dota2.DOTA2_MATCH.DOTA_EVENTS` AS c
  ON
    a.match_id = c.match_id
    AND a.hero_id = c.hero_id
  WHERE
    a.hero_id = 1
    AND (a.item_0 = 145
      OR a.item_1 = 145
      OR a.item_2 = 145
      OR a.item_3 = 145
      OR a.item_4 = 145
      OR a.item_5 = 145)
    AND c.event = 'purchase'
    AND c.key = 'bfury'
    AND a.isRadiant = true),
  temp2 AS(
  SELECT
    a.match_id,
    b.minute,
    b.gold_or_xp,
    b.value
  FROM
    temp1 AS a
  INNER JOIN
    `personal-project-for-dota2.DOTA2_MATCH.DOTA_ADVANTAGES` AS b
  ON
    a.match_id = b.match_id
  WHERE
    ROUND(a.time/60, 0) = b.minute
    AND b.minute < 50
--     AND b.value < 0
  ORDER BY
    match_id),
    
  temp3 AS(
  SELECT
    DISTINCT a.match_id,
    b.minute
  FROM (
    SELECT
      match_id,
      COUNT(gold_or_xp) AS c
    FROM
      temp2
    GROUP BY
      1) AS a
  INNER JOIN
    temp2 AS b
  ON
    a.match_id = b.match_id
  WHERE
    c > 1)

SELECT minute, count(match_id) AS a, count(IF(radiant_win=true, TRUE, NULL)) as win
FROM(
SELECT
  distinct b.match_id,
  a.minute,
  c.radiant_win
FROM
  `personal-project-for-dota2.DOTA2_MATCH.DOTA_ADVANTAGES` AS a,
  temp3 AS b,
  `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as c
WHERE
  a.match_id = b.match_id
  AND a.match_id = c.match_id
  AND a.minute = b.minute
ORDER BY
  match_id,
  minute)
GROUP BY 1
ORDER BY 1
"""

#Team_when_buy_bfury
analytic_3_team =  """
WITH
  temp1 AS(
  SELECT
    DISTINCT a.match_id,
    c.time
  FROM
    `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS` AS a
  INNER JOIN
    `personal-project-for-dota2.DOTA2_MATCH.DOTA_EVENTS` AS c
  ON
    a.match_id = c.match_id
    AND a.hero_id = c.hero_id
  WHERE
    a.hero_id = 1
    AND (a.item_0 = 145
      OR a.item_1 = 145
      OR a.item_2 = 145
      OR a.item_3 = 145
      OR a.item_4 = 145
      OR a.item_5 = 145)
    AND c.event = 'purchase'
    AND c.key = 'bfury'
    AND a.isRadiant = true),
  temp2 AS(
  SELECT
    a.match_id,
    b.minute,
    b.gold_or_xp,
    b.value
  FROM
    temp1 AS a
  INNER JOIN
    `personal-project-for-dota2.DOTA2_MATCH.DOTA_ADVANTAGES` AS b
  ON
    a.match_id = b.match_id
  WHERE
    ROUND(a.time/60, 0) = b.minute
    AND b.minute < 50
--     AND b.value < 0
  ORDER BY
    match_id),
    
  temp3 AS(
  SELECT
    DISTINCT a.match_id,
    b.minute
  FROM (
    SELECT
      match_id,
      COUNT(gold_or_xp) AS c
    FROM
      temp2
    GROUP BY
      1) AS a
  INNER JOIN
    temp2 AS b
  ON
    a.match_id = b.match_id
  WHERE
    c > 1)
SELECT
  b.match_id,
  a.minute,
  a.gold_or_xp,
  a.value,
FROM
  `personal-project-for-dota2.DOTA2_MATCH.DOTA_ADVANTAGES` AS a,
  temp3 AS b
WHERE
  a.match_id = b.match_id
  AND a.minute >= b.minute
ORDER BY
  match_id,
  minute
"""

analytic_3_equipment = """
SELECT a.key, a.v
FROM(
SELECT key, COUNT(key) as v
FROM `personal-project-for-dota2.DOTA2_MATCH.DOTA_EVENTS` 
WHERE hero_id = 1
AND event = 'purchase'
GROUP BY 1
ORDER BY v DESC) as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.ITEM_IDS` as b
ON a.key = b.item_name
WHERE val = 1
ORDER BY v DESC
LIMIT 10
"""

analytic_4_effect = """
SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
(SELECT b.match_id, b.gold_or_xp, b.value
FROM(
SELECT match_id, max(minute) AS max_minute
FROM `personal-project-for-dota2.DOTA2_MATCH.DOTA_ADVANTAGES` 
GROUP BY 1) as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_ADVANTAGES`  as b
ON a.match_id = b.match_id
AND a.max_minute = b.minute
ORDER BY 1) as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
ORDER BY 1
"""

analytic_4_count = """
WITH temp1 as
(SELECT b.match_id, b.gold_or_xp, b.value
FROM(
SELECT match_id, max(minute) AS max_minute
FROM `personal-project-for-dota2.DOTA2_MATCH.DOTA_ADVANTAGES` 
GROUP BY 1) as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_ADVANTAGES`  as b
ON a.match_id = b.match_id
AND a.max_minute = b.minute
ORDER BY 1)

SELECT 'pp+' as type, COUNT(DISTINCT a.match_id) as value
FROM
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 0
AND a.value > 0
AND b.radiant_win = true) as a
INNER JOIN 
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 1
AND a.value > 0
AND b.radiant_win = true) as b
ON a.match_id = b.match_id

UNION ALL 

SELECT 'pp-' as type, COUNT(DISTINCT a.match_id) as value
FROM
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 0
AND a.value > 0
AND b.radiant_win = false) as a
INNER JOIN 
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 1
AND a.value > 0
AND b.radiant_win = false) as b
ON a.match_id = b.match_id

UNION ALL 

SELECT 'pn+' as type, COUNT(DISTINCT a.match_id) as value
FROM
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 0
AND a.value > 0
AND b.radiant_win = true) as a
INNER JOIN 
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 1
AND a.value < 0
AND b.radiant_win = true) as b
ON a.match_id = b.match_id

UNION ALL 

SELECT 'pn-' as type, COUNT(DISTINCT a.match_id) as value
FROM
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 0
AND a.value > 0
AND b.radiant_win = false) as a
INNER JOIN 
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 1
AND a.value < 0
AND b.radiant_win = false) as b
ON a.match_id = b.match_id

UNION ALL

SELECT 'nn+' as type ,COUNT(DISTINCT a.match_id) as value
FROM
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 0
AND a.value < 0
AND b.radiant_win = true) as a
INNER JOIN 
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 1
AND a.value < 0
AND b.radiant_win = true) as b
ON a.match_id = b.match_id

UNION ALL 

SELECT 'nn-' as type, COUNT(DISTINCT a.match_id) as value
FROM
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 0
AND a.value < 0
AND b.radiant_win = false) as a
INNER JOIN 
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 1
AND a.value < 0
AND b.radiant_win = false) as b
ON a.match_id = b.match_id

UNION ALL

SELECT 'np+' as type, COUNT(DISTINCT a.match_id) as value
FROM
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 0
AND a.value < 0
AND b.radiant_win = true) as a
INNER JOIN 
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 1
AND a.value > 0
AND b.radiant_win = true) as b
ON a.match_id = b.match_id

UNION ALL 

SELECT 'np-' as type, COUNT(DISTINCT a.match_id) as value
FROM
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 0
AND a.value < 0
AND b.radiant_win = false) as a
INNER JOIN 
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 1
AND a.value > 0
AND b.radiant_win = false) as b
ON a.match_id = b.match_id
ORDER BY type
"""

analytic_4_gold = '''
WITH temp1 as
(SELECT b.match_id, b.gold_or_xp, b.value
FROM(
SELECT match_id, max(minute) AS max_minute
FROM `personal-project-for-dota2.DOTA2_MATCH.DOTA_ADVANTAGES` 
GROUP BY 1) as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_ADVANTAGES`  as b
ON a.match_id = b.match_id
AND a.max_minute = b.minute
ORDER BY 1), 
temp2 as
(SELECT a.match_id
FROM
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 0
AND a.value > 0
AND b.radiant_win = false) as a
INNER JOIN 
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 1
AND a.value > 0
AND b.radiant_win = false) as b
ON a.match_id = b.match_id)

SELECT 1 as t, count(b.value) AS val
FROM
temp2 as a
INNER JOIN temp1 as b
ON a.match_id = b.match_id
WHERE b.gold_or_xp = 0
AND b.value <= 5000

UNION ALL 

SELECT 2 as t ,count(b.value) as val
FROM
temp2 as a
INNER JOIN temp1 as b
ON a.match_id = b.match_id
WHERE b.gold_or_xp = 0
AND b.value <= 10000
AND b.value > 5000

UNION ALL

SELECT 3 as t, count(b.value) as val
FROM
temp2 as a
INNER JOIN temp1 as b
ON a.match_id = b.match_id
WHERE b.gold_or_xp = 0
AND b.value <= 15000
AND b.value > 10000

UNION ALL 

SELECT 4 as t ,count(b.value) as val
FROM
temp2 as a
INNER JOIN temp1 as b
ON a.match_id = b.match_id
WHERE b.gold_or_xp = 0
AND b.value <= 20000
AND b.value > 15000

UNION ALL 

SELECT 5 as t, count(b.value) as val
FROM
temp2 as a
INNER JOIN temp1 as b
ON a.match_id = b.match_id
WHERE b.gold_or_xp = 0
AND b.value > 20000
'''

analytic_4_xp = '''
WITH temp1 as
(SELECT b.match_id, b.gold_or_xp, b.value
FROM(
SELECT match_id, max(minute) AS max_minute
FROM `personal-project-for-dota2.DOTA2_MATCH.DOTA_ADVANTAGES` 
GROUP BY 1) as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_ADVANTAGES`  as b
ON a.match_id = b.match_id
AND a.max_minute = b.minute
ORDER BY 1), 
temp2 as
(SELECT a.match_id
FROM
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 0
AND a.value > 0
AND b.radiant_win = false) as a
INNER JOIN 
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 1
AND a.value > 0
AND b.radiant_win = false) as b
ON a.match_id = b.match_id)

SELECT 1 as t, count(b.value) AS val
FROM
temp2 as a
INNER JOIN temp1 as b
ON a.match_id = b.match_id
WHERE b.gold_or_xp = 1
AND b.value <= 5000

UNION ALL 

SELECT 2 as t ,count(b.value) as val
FROM
temp2 as a
INNER JOIN temp1 as b
ON a.match_id = b.match_id
WHERE b.gold_or_xp = 1
AND b.value <= 10000
AND b.value > 5000

UNION ALL

SELECT 3 as t, count(b.value) as val
FROM
temp2 as a
INNER JOIN temp1 as b
ON a.match_id = b.match_id
WHERE b.gold_or_xp = 1
AND b.value <= 15000
AND b.value > 10000

UNION ALL 

SELECT 4 as t ,count(b.value) as val
FROM
temp2 as a
INNER JOIN temp1 as b
ON a.match_id = b.match_id
WHERE b.gold_or_xp = 1
AND b.value <= 20000
AND b.value > 15000

UNION ALL 

SELECT 5 as t, count(b.value) as val
FROM
temp2 as a
INNER JOIN temp1 as b
ON a.match_id = b.match_id
WHERE b.gold_or_xp = 1
AND b.value > 20000
'''

analytic_4_d = """
WITH temp1 as
(SELECT b.match_id, b.gold_or_xp, b.value
FROM(
SELECT match_id, max(minute) AS max_minute
FROM `personal-project-for-dota2.DOTA2_MATCH.DOTA_ADVANTAGES` 
GROUP BY 1) as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_ADVANTAGES`  as b
ON a.match_id = b.match_id
AND a.max_minute = b.minute
ORDER BY 1), 
temp2 as
(SELECT a.match_id
FROM
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 0
AND a.value > 0
AND b.radiant_win = false) as a
INNER JOIN 
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 1
AND a.value > 0
AND b.radiant_win = false) as b
ON a.match_id = b.match_id),
temp3 as
(SELECT a.match_id, b.gold_or_xp, b.value
FROM
(SELECT a.match_id
FROM
temp2 as a
INNER JOIN temp1 as b
ON a.match_id = b.match_id
WHERE b.gold_or_xp = 1
AND b.value > 20000) as a
INNER JOIN temp1 as b
ON a.match_id = b.match_id
WHERE b.gold_or_xp = 0)

sELECT 1 as type, count(value) as v
from 
temp3 as a
WHERE value <= 5000

UNION ALL 

sELECT 2 as type, count(value) as v
from 
temp3 as a
WHERE value <= 10000
AND value > 5000

UNION ALL 

sELECT 3 as type, count(value) as v
from 
temp3 as a
WHERE value <= 15000
AND value > 10000

UNION ALL 

sELECT 4 as type, count(value) as v
from 
temp3 as a
WHERE value <= 20000
AND value > 15000

UNION ALL 

sELECT 5 as type, count(value) as v
from 
temp3 as a
WHERE value > 20000
"""

analytic_4_hero = """
WITH temp1 as
(SELECT b.match_id, b.gold_or_xp, b.value
FROM(
SELECT match_id, max(minute) AS max_minute
FROM `personal-project-for-dota2.DOTA2_MATCH.DOTA_ADVANTAGES` 
GROUP BY 1) as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_ADVANTAGES`  as b
ON a.match_id = b.match_id
AND a.max_minute = b.minute
ORDER BY 1),

temp2 as
(SELECT a.match_id
FROM
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 0
AND a.value > 0
AND b.radiant_win = false) as a
INNER JOIN 
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 1
AND a.value > 0
AND b.radiant_win = false) as b
ON a.match_id = b.match_id),

temp3 as
(SELECT a.match_id
FROM
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 0
AND a.value < 0
AND b.radiant_win = true) as a
INNER JOIN 
(SELECT a.match_id, a.gold_or_xp, a.value, b.radiant_win
FROM
temp1 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`  as b
ON a.match_id = b.match_id
WHERE a.gold_or_xp = 1
AND a.value < 0
AND b.radiant_win = true) as b
ON a.match_id = b.match_id)

SELECT hero_id, count(hero_id) as value
FROM
(SELECT b.match_id, b.hero_id
FROM temp2 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS`  as b
ON a.match_id = b.match_id
WHERE b.isRadiant is true

UNION ALL

SELECT b.match_id, b.hero_id
FROM temp3 as a
INNER JOIN `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS`  as b
ON a.match_id = b.match_id
WHERE b.isRadiant is false)
group by 1
order  by 2 DESC
LIMIT 10
"""

analytic_top1 = """
SELECT COUNT(IF(skill = 1, True, NULL)) as normal, COUNT(IF(skill = 2, True, NULL)) as hard, COUNT(IF(skill = 3, True, NULL)) as veryhard
FROM 
`personal-project-for-dota2.DOTA2_MATCH.DOTA_MATCH`
"""

analytic_top2 = """
select sum(kills) as kill , sum(deaths) as death, sum(assists) as assists
from `personal-project-for-dota2.DOTA2_MATCH.DOTA_PALYERS` 
"""