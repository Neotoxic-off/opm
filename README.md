# opm
Own Package Manager

## Download

```
git clone https://github.com/Neotoxic-off/opm
cd opm
```

## Output example
```
neo@endeavous -> ./opm 

:: loading packages
   -- packages loaded
:: extracting packages
   -- Abstrakt extracted
   -- packages extracted: 1
:: downloading Abstrakt
   -- downloaded
:: building Abstrakt
```

## Packages format

- [X] : `name: package name`
- [X] : `method: method to download package`
- [X] : `source: url of the source`
- [X] : `build: script to execute if build is required`

#### Template

```JSON
{
    "packages" : [
        {
            "name" : "my package name",
            "method" : "example of method",
            "source" : "source's url",
            "build" : "cd example ; make"
        }
    ]
}
```

#### Example

```JSON
{
    "packages" : [
        {
            "name" : "opm",
            "method" : "git clone",
            "source" : "https://github.com/Neotoxic-off/opm",
            "build" : "cd opm ; echo \"Opm is ready\""
        }
    ]
}
```

