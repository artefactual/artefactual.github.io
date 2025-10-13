Dependencies
============

Here is a list of dependencies for projects we maintain.

AtoM
----

All AtoM dependencies are external and are not being maintained by Artefactual.

Archivematica
-------------

Archivematica consists of several projects working together.

- `Archivematica <https://github.com/artefactual/archivematica>`__: Main repository containing the user-facing dashboard, task manager MCPServer and clients scripts for the MCPClient.
  - and the related `Archivematica documentation <https://github.com/artefactual/archivematica-docs>`__ repository.
- `Storage Service <https://github.com/artefactual/archivematica-storage-service>`__: Responsible for moving files to Archivematica for processing, and from Archivematica into storage
  - and the associated `Storage Service Documentation <https://github.com/artefactual/archivematica-storage-service-docs>`__

There are also several smaller repositories that support Archivematica in
various ways. In general, you will not need these to develop on Archivematica.

- `AM client <https://github.com/artefactual-labs/amclient>`__ : Archivematica API client module
- `AMmcpc <https://github.com/artefactual-labs/ammcpc>`__ : Archivematica MediaConch policy check wrapper
- `Automation Tools <https://github.com/artefactual/automation-tools>`__: Scripts used to automate processing material through Archivematica
- `Deployment <https://github.com/artefactual/deploy-pub>`__: Ansible scripts for deploying and configuring Archivematica
- `ansible-archivematica-src <https://github.com/artefactual-labs/ansible-archivematica-src>`__: Ansible role for Archivematica package install.
- `Fixity checker <https://github.com/artefactual/fixity>`__: Commandline tool that assists in checking fixity for AIPs stored in Archivematica Storage Service instances.
- `METS reader/writer <https://github.com/artefactual-labs/mets-reader-writer>`__: Library to create and parse METS files.
- `agentarchives <https://github.com/artefactual-labs/agentarchives>`__: Clients to retrieve, add, and modify records from archival management systems.
- `Sample data <https://github.com/artefactual/archivematica-sampledata>`__: Data to test and show off Archivematica's processing

If you are curious about where the code comes from, checkout the `History <https://github.com/artefactual/archivematica-history>`__ repository: Contains the pre-git history of Archivematica.
