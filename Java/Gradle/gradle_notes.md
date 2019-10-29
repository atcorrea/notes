# Gradle

## Dependencies
> Dependency configuration is nothing but defines set of dependences. You can use this feature to declare external dependences means which you want to download from the web. This defines different standers such as follows.
### Repositories
> While adding external dependencies. Gradle looks for them in a repository. A repository is just a collection of files, organized by group, name and version. By default, Gradle does not define any //repositories. We have to define at least one repository explicitly.//
```java
plugins {
   id 'java'
}

repositories {
   mavenCentral()
}

dependencies {
   compile group: 'org.hibernate', name: 'hibernate-core', version: '3.6.7.Final'
   testCompile group: 'junit', name: 'junit', version: '4.+'
}
```


## Plugins
> Plugin is nothing but set of tasks, almost all useful tasks such as compiling tasks, setting domain objects, setting up source files, etc are handled by plugins. Applying a plugin to a project means that allows the plugin to extend the project’s capabilities.

## Listing Projects
> You can list the project hierarchy of the selected project and their sub projects using gradle –q projects command. Here is the example, use the following command to list all the project in the build file.
```
C:\> gradle -q projects
```

## Listing Tasks for a project
> You can list all the tasks which belong to a project by using the following command.
```
C:\> gradle project:tasks --all
```
## Listing Dependencies for a project
> You can list all the dependencies which belong to a project by using the following command.
```
C:\> gradle project:tasks
```

## Referências
- https://www.tutorialspoint.com/gradle