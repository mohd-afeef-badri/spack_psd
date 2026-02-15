# PSD Spack Repository

Custom Spack repository for installing [PSD](https://github.com/mohd-afeef-badri/psd) - a massively parallel finite element solver for continuum dynamics.

## Quick Start
### 1. Install Spack

```sh
git clone --depth=2 https://github.com/spack/spack.git
```

### 2. Set Up Spack Environment
```sh
source /path/to/spack/share/spack/setup-env.sh
```
**Tip**: Add this line to your `~/.bashrc` or `~/.zshrc` for automatic loading:
```sh
echo 'source /path/to/spack/share/spack/setup-env.sh' >> ~/.bashrc
```

### 3. Add PSD Repository
Clone this repository:
```sh
git clone https://github.com/mohd-afeef-badri/spack_psd
```

Add it to Spack:
```sh
spack repo add /path/to/spack_psd/spack_repo/psd
```

### 4. Install PSD
```sh
spack install psd
```

### 5. Load PSD
After installation, load PSD into your environment:
```sh
spack load psd
```

## Verification

Verify the installation:
```sh
spack find psd
```

## Customization

To install with specific options:
```sh
# View available variants
spack info psd

# Install with custom variants
spack install psd +variant_name
```

## Uninstalling

```sh
spack uninstall psd
```

## License

This Spack package follows the same license as PSD: [Apache-2.0](LICENSE)
