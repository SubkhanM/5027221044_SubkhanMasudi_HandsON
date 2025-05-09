# SSH Practice

## 1. Generate SSH Key Pair
```bash
ssh-keygen -t rsa -b 2048 -C "your_email@example.com"
```

## 2. Copy Public Key ke Server
```bash
ssh-copy-id username@host_ip
```

## 3. Coba Koneksi Tanpa Password
```bash
ssh username@host_ip
```

## 4. Catatan Tambahan
- Default folder key: `~/.ssh/`
- File penting: `id_rsa` (private), `id_rsa.pub` (public)
