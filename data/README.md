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

- myWord : https://github.com/ye-kyaw-thu/myWord#Syllable-Segmentation-with-myWord-Segmentation-Tool

Dictionaries ​တွေ ​ဆောက်ဖို့က​တော့ myWord tool က word_dict.py ကို ပြင်ထားပါတယ်။ ပြင်ထားတဲ့ ​နေရာ​လေး​တွေ မှတ်ထား​ပေးပါတယ်။
Original ကို python file မှာ Comment အ​နေနဲ့ သိမ်းထားပါတယ်။

ကိုယ်ကြိုက်တဲ့ Corpus နဲ့ dictionaries ​ဆောက်ချင်ရင်​တော့ ဒီလို တန်း ​ဆောက် နိုင်ပါတယ်။ 
```{r, engine='bash', count_lines}
python build_dict.py -i myPOS.word
```
syllable level dictionary ကို myWord သုံး ဆောက်ပါတယ်။
```{r, engine='bash', count_lines}
python myword.py syllable myPOS.word myPOS.syllable
```

```{r, engine='bash', count_lines}
head -5 myPOS.syllable 
ဒီ ဆေး က ၁ ၀ ၀ ရာ ခိုင် နှုန်း ဆေး ဘက် ဝင် အ ပင် များ မှ ဖော် စပ် ထား တာ ဖြစ် တယ် ။
အ သစ် ဝယ် ထား တဲ့ ဆွယ် တာ က အ သီး ထ နေ ပါ ပေါ့ ။
မ ကျန်း မာ လျှင် နတ် ဆ ရာ ထံ မေး မြန်း ၍ သက် ဆိုင် ရာ နတ် တို့ အား ပူ ဇော် ပ သ ရ သည် ။
ပေ ဟိုင် ဥ ယျာဉ် ။
န ဝ မ အိပ် မက် ကော သ လ မင်း အိပ် မက် ၉ နက် ရှိုင်း ကျယ် ဝန်း သော ရေ ကန် ကြီး တစ် ခု တွင် သတ္တ ဝါ တို့ ဆင်း ၍ ရေ သောက် ကြ ၏ ။
```

```{r, engine='bash', count_lines}
python build_dict.py -i myPOS.syllable
```

```{r, engine='bash', count_lines}
head -5 small_frequency_dictionary_mm.syl 
ဒီ 5048
ဆေး 918
က 12216
၁ 3007
၀ 2139

head -5 small_frequency_bigram_dictionary_mm.syl 
 ဒီ ဆေး 40
 ဆေး က 11
 က ၁ 58
 ၁ ၀ 318
 ၀ ၀ 669
```


Ref :
- [1] https://github.com/ye-kyaw-thu/myPOS
- [2] https://github.com/ye-kyaw-thu/tools
- [3] https://github.com/ye-kyaw-thu/myWord#Syllable-Segmentation-with-myWord-Segmentation-Tool
