
# docker-print-dir-test

Simple test for printing the contents of the Docker container's filesytem

Build the image and name it as "print-dir" using the following command:

```bash
docker build -t print-dir .
```

Run the image in a container using the following command:

```bash
docker run -it --rm print-dir
```

Expected output is the contents of the top-level directory of the Docker
container's filesystem, as follows:

```
cwd:  /
Files:  usr, .dockerenv, etc, dev, Dockerfile, .git, README.md, printfs.py, root
, tmp, var, bin, lib, sbin, run, home, media, opt, proc, lib64, boot, srv, sys,
mnt
```
