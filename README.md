# Petool

This is a tool for dealing with savefiles from http://petscii.krissz.hu/.

Currently only minimum viable tool that will decrompress the data field of
saved .pe file. Usefull for pipeing into other json tools.

## Example usage

Extract data field as json.

```bash
cat my_project.pe | python3 pytool.py | jq -C ".data | fromjson"
```

