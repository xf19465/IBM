SELECT owner.owner_id as "owner_id" , owner.owner_name as "owner_name" , COUNT(DISTINCT(cam.category_id)) AS "different_category_count"
FROM `owner` owner, `article` art, `category_article_mapping` cam
WHERE art.owner_id = owner.owner_id
AND cam.article_id = art.article_id
ORDER BY COUNT(DISTINCT(cam.category_id))