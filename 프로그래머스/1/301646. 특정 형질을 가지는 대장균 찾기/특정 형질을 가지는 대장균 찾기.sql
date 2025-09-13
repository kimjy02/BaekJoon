SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE (GENOTYPE & 2) = 0                 -- 2번 형질 없음
  AND ( (GENOTYPE & 1) > 0               -- 1번 형질 있거나
     OR (GENOTYPE & 4) > 0 );            -- 3번 형질 있음
