# 수행 로그

## Git 저장소 복제 실습

```
$ git clone https://github.com/cla7shade/codyssey-academy.git /tmp/codyssey-clone
Cloning into '/tmp/codyssey-clone'...
```

```
$ ls /tmp/codyssey-clone
e1-1
e1-2
```

```
$ git -C /tmp/codyssey-clone log --oneline -3
43a8655 docs(e1-2): add Git basics notes to README
40ffa3f docs(e1-2): write project README with overview, usage, and state.json schema
ac0c9ea feat(e1-2): implement score check feature
```

```
$ echo '<!-- clone/pull 실습 -->' >> /tmp/codyssey-clone/e1-2/README.md
$ git -C /tmp/codyssey-clone diff e1-2/README.md
diff --git a/e1-2/README.md b/e1-2/README.md
index d1fb710..be667bf 100644
--- a/e1-2/README.md
+++ b/e1-2/README.md
@@ -279,3 +279,4 @@ git commit -m "init"
 git remote add origin https://github.com/유저명/저장소명.git  # origin은 원격 저장소에 붙이는 별칭
 git push -u origin main  # -u로 upstream 설정
 ```
+<!-- clone/pull 실습 -->
```

```
$ git -C /tmp/codyssey-clone add e1-2/README.md
$ git -C /tmp/codyssey-clone commit -m 'docs(e1-2): clone/pull 실습용 변경'
[main 6abb6cb] docs(e1-2): clone/pull 실습용 변경
 1 file changed, 1 insertion(+)
```

```
$ git -C /tmp/codyssey-clone push origin main
To https://github.com/cla7shade/codyssey-academy.git
   43a8655..6abb6cb  main -> main
```

```
$ git -C /Users/cla6shade8560/codyssey-academy pull origin main
From https://github.com/cla7shade/codyssey-academy
 * branch            main       -> FETCH_HEAD
   43a8655..6abb6cb  main       -> origin/main
Updating 43a8655..6abb6cb
Fast-forward
 e1-2/README.md | 1 +
 1 file changed, 1 insertion(+)
```

```
$ git -C /Users/cla6shade8560/codyssey-academy log --oneline -5
6abb6cb docs(e1-2): clone/pull 실습용 변경
43a8655 docs(e1-2): add Git basics notes to README
40ffa3f docs(e1-2): write project README with overview, usage, and state.json schema
ac0c9ea feat(e1-2): implement score check feature
c5f8886 feat(e1-2): implement quiz list feature
```

```
$ tail -3 /Users/cla6shade8560/codyssey-academy/e1-2/README.md
git push -u origin main  # -u로 upstream 설정
```
<!-- clone/pull 실습 -->
```
