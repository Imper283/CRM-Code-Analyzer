import os
import json

def scan(path):
    # Проверяем наличие ESLint в package.json
    package_json_path = os.path.join(path, 'package.json')
    has_eslint_dependency = False
    
    if os.path.exists(package_json_path):
        with open(package_json_path, 'r', encoding='utf-8') as f:
            try:
                package_data = json.load(f)
                dependencies = package_data.get('dependencies', {})
                dev_dependencies = package_data.get('devDependencies', {})
                has_eslint_dependency = 'eslint' in dependencies or 'eslint' in dev_dependencies
            except json.JSONDecodeError:
                return ["package.json не является валидным JSON файлом", False, False, False]
    else:
        return ["Отсутствует package.json файл в указанной директории", False, False, True]

    # Проверяем наличие ESLint конфиг файла
    eslint_config_files = [
        '.eslintrc',
        '.eslintrc.js',
        '.eslintrc.cjs',
        '.eslintrc.yaml',
        '.eslintrc.yml',
        '.eslintrc.json',
        'eslint.config.js',
        'eslint.config.mjs'
    ]
    
    has_eslint_config = any(
        os.path.exists(os.path.join(path, config_file))
        for config_file in eslint_config_files
    )

    if has_eslint_dependency and has_eslint_config:
        return ["ESLint и его конфигурационный файл найдены.", True, True, False]
    elif has_eslint_dependency and not has_eslint_config:
        return ["ESLint найден в зависимостях, но конфигурационный файл отсутствует.", True, False, False]
    elif not has_eslint_dependency and has_eslint_config:
        return ["Конфигурационный файл ESLint найден, но сам ESLint не установлен как зависимость.", False, True, False]
    else:
        return ["ESLint и его конфигурационный файл отсутствуют.", False, False, False]
    