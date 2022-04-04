# Erste Gehversuche mit odoo
- am besten sich mit dem container verbinden.

# Meine Erste schritte und Erfahrungen mit Odoo
- Starten eines neues Projektes vom scratch
  - Siehe das docker-compose.yml
  - wichtig lege einen file mit dem name **"odoo_pg_pass"** an.
    - Trage einen Passwort in die erste Zeile ein.
  - Einfach beim ersten mal mit "docker-compose up --build" die Anwendung erstellen.
  - [im browser](http:localhost:http://localhost:8069/) aufrufen
  - und einmal einrichten lassen.
  - Fertig

<hr>

## Erste schritte mit der RestAPI
### odoo:15 hat einige Veränderungen mitgebracht
- Erste Herausforderung, **odoo-bin** heist jetzt nur noch odoo
- habe mit dem odoo scaffold einen neuen controller angelegt
  - Entweder innerhalb des attach docker container mit
    ```bash
    odoo scaffold dataholix-web /mnt/extra-addons
    ```
  - oder über docker direkt
    ```bash
    docker exec -ti odoo_container_name odoo scaffold /mnt/extra-addons dataholix-web
    ```
  - docker-compose wäre noch eine Möglichkeit
    ```bash
    docker-compose exec web odoo scaffold dataholix-web /mnt/extra-addons
    ```

### Aufruf der Seite nach dem start der compose Anweisung
- Im Browser https://localhost:8069