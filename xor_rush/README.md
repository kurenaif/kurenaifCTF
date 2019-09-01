flag format: `kurenaifCTF{*}`

# xor rush

この問題はハッシュ化の性質上、別の文字列でも同じハッシュ値を示してしまいます。
なので、文字列を与えると順列を整えるプログラムを作成しています。
ぜひご利用ください。

```
$ python3 recover.py kurenaifCTF{}hogehoge
nuohogkhTee{gefCaFri}

$python3 recover.py CTFkurenaif\{hogehoge\}
nuohogkhTee{gefCaFri}
```
↑ 順列が違う文字列を与えていますが、同じ結果を返しています。
順列が異なっていても、文字が正しければフラグが出てきます