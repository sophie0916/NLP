import re

def dollar(text):
    count = 0
    exp = "(((\$[\s]?[0-9,]+(.[0-9]{2})?)(\s)?((billion)|(million)|(trillion))?((\s)[Dd]ollars)?)|([0-9,]+(\s)?[Dd]ollars)|((\$)?(((half)|(quarter))(\s)of(\s))?([a-zA-z]+)\s[Dd]ollar[s]?))"
    d_output = open("dollar_output.txt", "w")
    d_list = open("dollar_list.txt", "w")
    out_text = text
    for item in re.finditer(exp, text):
        d_list.write(item.group(0).replace('\n',' '))
        d_list.write('\n')
        out_text = out_text[:item.start()+(count*2)] + "[" + item.group(0) + "]" + out_text[item.end()+(count*2):]
        count+=1
    d_output.write(out_text)
    d_list.close()
    d_output.close()
    print("Dollar count is: " + str(count))

def phone(text):
    count = 0
    exp = "((([(][0-9]{3}[)])|([0-9]{3}))[-.)\s]?(([0-9]{3}[-.\s]?[0-9]{4})|([a-zA-z]{3}[-.][a-zA-z]{4})))"
    p_output = open("phone_output.txt", "w")
    p_list = open("phone_list.txt", "w")
    out_text = text
    for item in re.finditer(exp, text):
        p_list.write(item.group(0).replace('\n',' '))
        p_list.write('\n')
        out_text = out_text[:item.start()+(count*2)] + "[" + item.group(0) + "]" + out_text[item.end()+(count*2):]
        count+=1
    p_output.write(out_text)
    p_list.close()
    p_output.close()
    print("Phone number count is: " + str(count))

if __name__ == "__main__":
    filename = "test_dollar_phone_corpus.txt"
    f = open(filename, "r")
    text = f.read()
    dollar(text)
    phone(text)
