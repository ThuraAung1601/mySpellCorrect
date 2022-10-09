## Data Preparation notes

အရင်ဆုံး ဆရာ ​ဒေါက်တာရဲ​ကျော်သူ ရဲ့ github က​နေ myPOS ver3.0 ကို သွား ​Download ပါတယ်။

```{r, engine='bash', count_lines}
wget https://github.com/ye-kyaw-thu/myPOS/blob/master/corpus-ver-3.0/corpus/mypos-ver.3.0.txt
```

ပြီး​တော့ ဆရာ ​ဒေါက်တာရဲ​ကျော်သူ ရဲ့ tools က rm-myPOStags.sh ကို သုံးပါတယ်။ 
https://github.com/ye-kyaw-thu/tools/blob/master/bash/rm-myPOStags.sh

Remove pipes
```{r, engine='bash', count_lines}
tr -s "|" " " < ./mypos-ver.3.0.txt > ./mypos-ver.3.0.nopipe.txt
```
Remove tags
```{r, engine='bash', count_lines}
./rm-myPOStags.sh
```

Dictionaries ​တွေ ​ဆောက်ဖို့က​တော့ myWord tool က word_dict.py ကို ပြင်ထားပါတယ်။ ပြင်ထားတဲ့ ​နေရာ​လေး​တွေ မှတ်ထား​ပေးပါတယ်။
Original ကို python file မှာ Comment အ​နေနဲ့ သိမ်းထားပါတယ်။

ကိုယ်ကြိုက်တဲ့ Corpus နဲ့ dictionaries ​ဆောက်ချင်ရင်​တော့ ဒီလို တန်း ​ဆောက် နိုင်ပါတယ်။ 
```{r, engine='bash', count_lines}
python build_dict.py -i corpus.txt
```

Ref :
- [1] https://github.com/ye-kyaw-thu/myPOS
- [2] https://github.com/ye-kyaw-thu/tools
