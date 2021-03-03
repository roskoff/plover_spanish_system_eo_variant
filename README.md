## [WIP] Plugin para Plover - Sistema Español (variante eo)

Este plugin es para [Plover](https://www.openstenoproject.org/plover/), herramienta que nos permite practicar estenotipia sin necesidad de tener un hardware especializado.

La implementación Sistema Español (variante eo) es una aproximación para utilizar la distribución del teclado americano aplicado a nuestro idioma.

### Definición del Sistema

#### Distribución (layout)

Utiliza distribución americana de teclas para estenotipia: `#STKPWHRAO*EUFRPBLGTSDZ`

![Steno Layout](https://i.imgur.com/sIuOpxu.png)

> Imagen tomada de [Art of chording](https://www.artofchording.com/introduction/how-steno-works.html#chords).

#### Alfabeto

Se puede deletrear el alfabeto con las siguientes combinaciones:

|||||||||
|---|---|---|---|---|---|---|---|
|`A*: a`|`PW*: b`|`KR*: c`|`TK*: d`|`*E: e`|`TP*: f`|`TKPW: g`|`H*: h`|
|`*EU: i`|`SKWR*: j`|`K*: k`|`HR*: l`|`PH*: m`|`TPH*: n`|`TPWH*: ñ`|`O*: o`|
|`P*: p`|`KW*: q`|`R*: r`|`S*: s`|`T*: t`|`*U: u`|`SR*: v`|`W*: w`|
|`KP*: x`|`KWR*: y`|`STKPW*: z`|`HA*: á`|`H*E: é`|`H*EU: í`|`HO*: ó`|`H*U: ú`|

#### Diccionarios

Incluye diccionarios por default:

- Artículos: Todos los artículos del español.
- Principal: Se pretende incluir aquí la mayor cantidad de entradas posibles, son todas las palabras en general que encontraremos en el español.
- Usuario: Orientado a cargas personalizadas de cada usuario.

> Observación: Durante el desarrollo utilizaré este diccionario para ir anotando nuevas entradas para desarrollar el sistema. Una vez que considere que se ajusta a las reglas que iré estableciendo, los graduaré al diccionario principal.

#### Sistema

Este sistema será predominantemente silábico. Por el momento, lo más apropiado que encuentro es ir creando la definición de las palabras basados en su construcción silábica. Habrán excepciones con respecto a las palabras más utilizadas según la lista de frecuencia de palabras encontrada en el [Corpus RAE](http://corpus.rae.es/lfrecuencias.html).

Por ejemplo, `"TK": "de"`, `"K": "que"`, `"P": "para"`, `"S": "es"` se encuentran entre las 15 palabras más frecuentes en el listado.

El `*` se utilizará como desambiguador principal en la mayoría de los casos, por ejemplo para representar acento diacrítico: por un lado `"SEU": "si"`, y por otro lado `"S*EU": "sí"`. En otros casos, como el de los *participios* o *vocales acentuadas*, se propone sumar `H` como desambiguador complementario, aprovechando su carácter de letra muda.

#### Plural de los sustantivos

Normalmente, se debería agregar sólo `-S` a un sustantivo para poder plurarizarlo.
> Basado en [El plural de los sustantivos en español](https://espanol.lingolia.com/es/gramatica/sustantivos/plural).

#### Participios

Se puede generar un participio en la mayoría de sus formas añadiendo:

- `TKHO*` (ado) y `TKHA*` (ada), para verbos que terminan en `ar`.
- `TKHA*EU` (ida) y `TKHO*EU` (ido), para verbos que terminan en `er` e `ir` (notar que el acorde está invertido).

> Basado en [El participio en español](https://espanol.lingolia.com/es/gramatica/verbos/participio).

#### Gerundios

Se puede generar un gerundio en la mayoría de sus formas añadiendo `-PBD` tanto para `ando`, `iendo` y varias formas irregulares.

#### Diptongos

Teniendo en cuenta las vocales abiertas `a`, `e`, `o` y las cerradas `i`, `u`; se pueden formar diptongos con las siguientes combinaciones:

- Dos vocales cerradas distintas:
  - `ui/uí`: ruido, construir, incluí. La `u` es parte de la `i` en el teclado, por lo tanto se propone usar `*EU`, así: `"R*EU/TKO": "ruido"`, `"KOPBS/TR*EUR": "construir"`, `"EUPB/KHR*EU": "incluí"`.
  - `iu/iú`: viuda, ciudad, siútico. Al igual que el anterior, pero utilizaríamos `*U`, así: `"SR*U/TKA": "viuda"`, `"S*U/TKAD": "ciudad"`, `"S*U/TEU/KO": "siútico"`.
- Vocal abierta tónica + vocal cerrada átona
  - `ai/ái`: aire,  paisaje, caída. Se puede combinar en el teclado con `AEU` y `A*EU`.
  - `au/áu`: aunque, causa, aún. Se puede combinar en el teclado con `AU` y `A*U`.
  - `ei/éi`: seis, aceite, alféizar. La `e` es parte de la `i` en el teclado, por lo tanto aquí la propuesta es ir con `*E` siempre que se pueda. Así: `"S*ES": "seis"`, `"A/S*E/TE": "aceite"`, `"AL/TP*E/SAR": "alféizar"`.
  - `eu/éu`: reunir, deuda, terapéutica. `EU` ya representa la vocal `i`, por lo tanto aquí la propuesta es ir con `*E` siempre que se pueda. Así: `"R*E/TPHEUR": "reunir"`, `"TK*E/TKA": "deuda"`, `"TE/RA/P*E/TEUBG": "terapéutica"`.
  - `oi/ói`: coincidir, moisés, oído. Se puede combinar en el teclado con `OEU`y `O*EU`.
  - `ou/óu`: aparentemente no hay ocurrencias de esta combinación o tal vez sean palabras muy raras. La combinación la usaremos invertida para otro grupo de diptongos más común: `uo/uó`.
- Vocal cerrada átona + vocal abierta tónica
  - `ia/iá`: social, familia, diálogo. Se propone utilizar sólo la vocal tónica combinada con `*` en el acorde, así: `"SO/SA*L": "social"`, `"TPA/PHEU/HRA*": "familia"`, `"TKA*/HRO/TKPWO": "diálogo"`.
  - `ie/ié`: tiene, tiempo, recién. Se propone usar de vuelta `*E`, así: `"T*E/TPHE": "tiene"`, `"T*EPL/PO": "tiempo"`, `"RE/S*EPB": "recién"`.
  - `io/ió`: nacional, espacio, relación. Se propone aquí `O*`, así: `"TPHA/SO*/TPHAL": "nacional"`, `"ES/PA/SO*": "espacio"`, `"RE/HRA/SO*PB": "relación"`.
  - `ua/uá`: situación, actual, zaguán. Se propone usar `A*`, así: `"SEU/TA*/SO*PB": "situación"`, `"ABG/TA*L": "actual"`, `"SA/TKPWA*PB": "zaguán"`.
  - `ue/ué`: pues, nuevo, huésped. Se propone usar de vuelta `*E`, así: `"P*ES": "pues"`, `"TPH*E/SRO": "nuevo"`, `"H*ES/PED": "huésped"`.
  - `uo/uó`: antiguo, individuo, actuó. Utilizaremos la combinación invertida del teclado: `OU` y `O*U`. Así: `"APB/TEU/TKPWOU": "antiguo"`, `"EUPB/TKEU/SREU/TKOU": "individuo"`, `"ABG/TO*U": "actuó"`.

- Ejemplos de palabras con más de un diptongo:
  - `"SKWR*EU/SO*": "juicio"`
  - `"R*E/TPHO*PB": "reunión"`
  - `"SEU/TA*/SO*PB": "situación"`

> Basado en [Diptongos, triptongos e hiatos](https://espanol.lingolia.com/es/redaccion/acentuacion#a-diptongos-triptongos-e-hiatos).


#### Casos especiales

- La letra `ll`: la idea es utilizar el sonido casi equivalente de la `y`, así: `"E/KWRA": "ella"`.

- La letra `s` intermedia: se toma la regla de la teoría de Plover que dice que podemos usar `-F` como si fuera una `S` en la parte intermedia de la palabra, por ejemplo: `"TKEFD": "desde"`.

- La letra `q (KW)`: esta letra no la utilizaríamos para las sílabas, en su reemplazo utilizamos directamente la `K`. Ej.: `"K*E": "qué"`.

- Abreviaciones comunes que podrían aparecer:
  - Usar `-T` para comprimir sílabas si la palabra termina en `te`. Ej.: `"TKU/RAPBT": "durante"`.
  - Usar `-D` para comprimir sílabas si la palabra termina en `de`. Ej.: `"SRERD": "verde"`.
  - Usar `-TS` para comprimir sílabas si la palabra termina en `tes` de por sí, o como plural de `te`. Ej.: `"TKA*/PWETS": "diabetes"` (no es plural), `"APBTS": "antes"` (no es plural), `"RE/S*EPBTS": "recientes"`.
  - Usar `S` para abreviar la sílaba inicial `es`.
  - USAR `BG` para comprimir sílabas si la palabra temina en `ca`. Ej.: `"PO/HREU/TEUBG": "política"`.

## Instalación

1. Abrir Plover
2. Ir al Plugin Manager
3. Elegir `plover-spanish-system-eo-variant` de la lista
4. Click en `Install/Update`
5. Reiniciar Plover

> Requiere Plover versión 4.0.0 o superior.

## Uso
Para activar el plugin, simplemente se debe elegir el sistema desde la configuración de `Plover`.

## Contribuciones
Los pull requests son bienvenidos. Para cambios sustanciales, por favor abrí antes un issue para discutir el cambio que quieras realizar.

Asegurate de actualizar los tests apropiadamente cuando el caso lo requiera.

## License
[GPLv2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html)