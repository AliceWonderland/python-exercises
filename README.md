# python_decoder

Decode an input.txt file made up of strs delimited by whitespace and newline. Example:

    "3 love\ncomputers\n2 dogs\n4 cats\n1 I\n5 you"

Using encoded numbers given in a pyramid scheme of last number in each newline formatted like this:

       1
      2 3
     4 5 6

Result should be:

    "I love computers"

Explanation:
    Each "encoded number" corresponds to a word.
    1: "I", 3: "love", 6: "computers"
    Use each "encoded number" to create a str of words resulting in the "decoded msg"

## To Use: 
* Use str formatted in key/value pairs delimited by space or newline.
* Place this in an input.txt file
* Run py file from command line using 'python ./decoder.py'

# Created Using Google IDX o.O
Get started by customizing your environment (defined in the .idx/dev.nix file) with the tools and IDE extensions you'll need for your project!

Learn more at https://developers.google.com/idx/guides/customize-idx-env


