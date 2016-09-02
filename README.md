Steps to show bug in Django/Selenium whereby it hangs.

# Reproduction Steps
1. Install chromedriver.
2. Create and activate a virtualenv.
3. Clone and install this project:

    ```
    git clone https://github.com/joshuablake/selenium
    cd selenium
    pip install -e .
    ./bug_hunt/manage.py test
    ```

Observe that the selenium browser hangs.
