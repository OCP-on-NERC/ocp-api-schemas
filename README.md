## Updating the schemas

1. Ensure you are authenticated to Kubernetes.

2. Update the extracted schemas:

    ```
    python extract-schemas.py -o schema.json
    ```

3. Commit your changes:

    ```
    git commit -m 'Updated schema repository'
    ```
