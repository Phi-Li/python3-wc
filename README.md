# python3-wc

## Releases

__!!!ATTENTION!!!__

As it is __NOT__ a good practice to commit large binary files directly to the repository, I put the `.exe` file in the releases page as Github suggests.

You can simply download it here:

(__你可以点此下载exe文件：__)

[wc.exe](https://github.com/Phi-Li/python3-wc/releases/download/v0.1/wc.exe)

(__若以上链接因为那个大家都懂的原因无法访问，请__ [https://pan.baidu.com/s/1yBWb07SrkY1d9RFEi7UL2Q](https://pan.baidu.com/s/1yBWb07SrkY1d9RFEi7UL2Q))

## Test cases

For Windows users, you can put `wc.exe` into `test` and then run `test.bat`. It will run the following tests automatically for you.

1. Input:

        python3 wc.py -clw case_1.txt

    or

        wc.exe -clw case_1.txt

    Expected output:

        case_1.txt, 行数: 1
        case_1.txt, 单词数: 2
        case_1.txt, 字符数: 30

1. Input:

        python3 wc.py -clw case_2.txt

    or

        wc.exe -clw case_2.txt

    Expected output:

        case_2.txt, 行数: 1
        case_2.txt, 单词数: 4
        case_2.txt, 字符数: 28

1. Input:

        python3 wc.py -clw case_3.txt

    or

        wc.exe -clw case_3.txt

    Expected output:

        case_3.txt, 行数: 2
        case_3.txt, 单词数: 5
        case_3.txt, 字符数: 33

1. Input:

        python3 wc.py -clw case_4.txt

    or

        wc.exe -clw case_4.txt

    Expected output:

        case_4.txt, 行数: 1
        case_4.txt, 单词数: 3
        case_4.txt, 字符数: 34

1. Input:

        python3 wc.py -clw case_5.txt

    or

        wc.exe -clw case_5.txt

    Expected output:

        case_5.txt, 行数: 2
        case_5.txt, 单词数: 6
        case_5.txt, 字符数: 47

1. Input:

        python3 wc.py -clw case_6.txt

    or

        wc.exe -clw case_6.txt

    Expected output:

        case_6.txt, 行数: 4
        case_6.txt, 单词数: 16
        case_6.txt, 字符数: 185

1. Input:

        python3 wc.py -a case_7.txt

    or

        wc.exe -a case_7.txt

    Expected output:

        case_7.txt, 代码行/空行/注释行: 13/2/7

1. Input:

        python3 wc.py -a case_8.txt

    or

        wc.exe -a case_8.txt

    Expected output:

        case_8.txt, 代码行/空行/注释行: 13/2/7

1. Input:

        python3 wc.py -w case_9.txt -e case_10.txt

    or

        wc.exe -w case_9.txt -e case_10.txt

    Expected output:

        case_9.txt, 单词数: 15

1. Input:

        python3 wc.py -w case_10.txt -e case_9.txt

    or

        wc.exe -w case_10.txt -e case_9.txt

    Expected output:

        case_10.txt, 单词数: 1
