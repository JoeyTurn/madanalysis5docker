# Updated 27.03.2023 to include LLP models for use in MG5, added for ease of access; models uploaded are from https://longlivedparticles.web.cern.ch/.

### Updated 07.03.2023 to include MadAnalysis5 and MadGraph5. They can be located in /MG5_aMC and /madanalysis respectively.

## This document is meant to be used to help set up MadAnalysis5 (https://github.com/MadAnalysis/madanalysis5) using Docker, as all other existing versions on Docker are outdated/non-functional.

After Docker Desktop is installer, head to https://hub.docker.com/repository/docker/joeyturn/madanalysis/general to learn more about the dockerfile and/or use docker push joeyturn/madanalysis:latest to pull the docker image to your docker installation. From there, open the <b>Images</b> tab on docker desktop and copy the string under joeyturn/madanalysis. With this in the clipboard, open a command prompt and type "docker run -dit -it ID" with ID being what is on the clipboard. This should send a string to the command prompt, and more importantly, open a new container which can be found inside the Docker Desktop tab.

With the container open, navigate to the terminal tab and type "bash" as this grant's access to arrow keys and tab auto-complete.

### Typing "./bin/ma5" inside /madanalysis/ will take you to the main part of MadAnalysis.

Installing extra packages such as fastjet/delphes/pad are recommended, and can be done so by typing "install" and finding the package to be installed. Note: installing normal PAD may not function at the moment, though the other two PAD packages should work just fine.

### The last major thing to do is to switch the rendering package from ROOT to matplotlib as ROOT doesn't currently function. This can be done by typing "set main.graphic_render = matplotlib".

Unfortunately this must be done every time the madanalysis5 terminal is opened; editing instillation_options.dat to bypass ROOT doesn't seem to function in docker while ROOT is still needed to download other packages.

From here, everything should be set up and ready to be used! Any questions about the docker setup or related can be sent to joeyturn@uw.edu, and questions regarding MadAnalysis5 can be sent to the email listed inside https://github.com/MadAnalysis/madanalysis5.
