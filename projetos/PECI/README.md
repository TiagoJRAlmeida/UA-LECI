# Folder with the final code

## How to run the code?

**NOTE:** This instructions presuppose that you will be using bash.

**1. Get inside the **src/** folder**

**2. Create a virtual enviroment and run it.**
  - How to create a virtual enviroment? Use the following command:
    ```bash
    python3 -m venv venv
    ```

  - How to run the virtual enviroment created? Use the following command:
    ```bash
    source venv/bin/activate
    ```

**3. Install the necessary dependencies using the command:**
```bash 
pip install -r requirements.txt
```

**4. After having the enviroment setuped, you can try the program with the command:**
```bash
python3 main.py
```

## Project Notes

- **The Ground Truth Synonym Map has the following format**

```json
{
  Name_variant: {
    Standard_name: [
      [
        Identification_number
      ]
    ] 
  },
  ...
  Name_variant_n: {
    Standard_name_n: [
      [
        Identification_number_n
      ]
    ] 
  }
}
```

- Possible question: Why is the **Name_variant** value a dictionary and the **Standard_name** value a list of lists?
  1. Because a given **Name_variant** might have multiple **Standard_names** associated with it. In that case, it must be choosen one manually.
  2. Because a given **Standard_name** might be connected to multiple **Identification_numbers**

  **NOTE: All this problems stem from the standard table being wrong. A lot is corrected automatically, but what isn't must be alerted to the user to be manually corrected.**      


- **The Final Version Synonym Map has the following format**
```json
{
  Name_variant1: Standard_name1,
  Name_variant2: Standard_name2,
  ...
  Name_variantN: Standard_nameN
}
```