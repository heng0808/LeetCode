# @param {String} path
# @return {String}
def simplify_path(path)
    splits = path.split '/'
    split_paths = []
    splits.each do |folder|
        if folder.length > 0
            if folder == '.'
                next
            elsif folder == '..'
                split_paths.pop
            else
                split_paths << folder
            end
        end
    end
    path = ''
    split_paths.each do |folder|
        path += '/'
        path += folder
    end
    if path.length == 0
        path = '/'
    end
    puts path
end

simplify_path "/home//foo/"
simplify_path "/home/"
simplify_path "/../"
simplify_path "/a/../../b/../c//.//"
simplify_path "/a/./b/../../c/"